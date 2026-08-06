import hashlib
import time

from openai import OpenAI

from app.core.config import OPENAI_API_KEY


class AustinAIGateway:
    """
    Production-safe AI gateway:
    - caching
    - GPT fallback handling
    - offline reasoning fallback
    """

    def __init__(self, memory_store=None):
        self.client = None
        self.cache = {}  # simple in-memory cache (upgrade later to Redis)
        self.memory_store = memory_store

        # cost controls (VERY important)
        self.max_requests_per_minute = 30
        self.request_timestamps = []

    # ----------------------------
    # RATE LIMIT GUARD
    # ----------------------------
    def _rate_limited(self):
        now = time.time()
        self.request_timestamps = [t for t in self.request_timestamps if now - t < 60]
        return len(self.request_timestamps) >= self.max_requests_per_minute

    def _log_request(self):
        self.request_timestamps.append(time.time())

    # ----------------------------
    # CACHE KEY
    # ----------------------------
    def _cache_key(self, query, analysis):
        raw = f"{query}:{analysis!s}"
        return hashlib.md5(raw.encode()).hexdigest()

    # ----------------------------
    # GPT CLIENT
    # ----------------------------
    def _get_client(self):
        if not OPENAI_API_KEY:
            return None
        if self.client is None:
            self.client = OpenAI(api_key=OPENAI_API_KEY)
        return self.client

    # ----------------------------
    # LOCAL FALLBACK ENGINE
    # ----------------------------
    def _local_reason(self, query, analysis):
        return f"""
Austin Local Intelligence Mode:

Query: {query}

Analysis:
{analysis}

Decision: processed using local reasoning engine (no GPT available or quota exceeded).
""".strip()

    # ----------------------------
    # MAIN ENTRY
    # ----------------------------
    def reason(self, query: str, analysis: dict):
        cache_key = self._cache_key(query, analysis)

        # 1. CACHE HIT
        if cache_key in self.cache:
            return self.cache[cache_key]

        # 2. RATE LIMIT CHECK
        if self._rate_limited():
            result = self._local_reason(query, analysis)
            self.cache[cache_key] = result
            return result

        client = self._get_client()

        # 3. NO API KEY → fallback
        if client is None:
            result = self._local_reason(query, analysis)
            self.cache[cache_key] = result
            return result

        self._log_request()

        prompt = f"""
You are Austin AI, a real estate intelligence system.

User Query:
{query}

Analysis:
{analysis}

Explain the decision clearly and briefly.
"""

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are Austin AI assistant."},
                    {"role": "user", "content": prompt},
                ],
            )

            result = response.choices[0].message.content

        except Exception:
            # ANY FAILURE → SAFE FALLBACK
            result = self._local_reason(query, analysis)

        # 4. CACHE RESULT
        self.cache[cache_key] = result

        return result
