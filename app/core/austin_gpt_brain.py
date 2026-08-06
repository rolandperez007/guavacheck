import hashlib
import os

from openai import OpenAI


class AustinGPTBrain:
    def __init__(self):
        self.client = None
        self.cache = {}

    def _get_client(self):
        if self.client is None:
            key = os.getenv("OPENAI_API_KEY")

            if not key:
                return None

            self.client = OpenAI(api_key=key)

        return self.client

    def _cache_key(self, query, analysis):
        raw = f"{query}-{analysis!s}"
        return hashlib.md5(raw.encode()).hexdigest()

    def _offline_reason(self, query, analysis):
        return f"""
Austin Offline Reasoning Mode:

Query: {query}

Analysis:
{analysis}

Decision: processed using rule-based engine only.
""".strip()

    def reason(self, query: str, analysis: dict):

        key = self._cache_key(query, analysis)

        # Cache hit
        if key in self.cache:
            return self.cache[key]

        client = self._get_client()

        # No OpenAI key
        if client is None:
            result = self._offline_reason(query, analysis)
            self.cache[key] = result
            return result

        try:
            prompt = f"""
You are Austin AI, a real estate intelligence system.

User Query:
{query}

Analysis:
{analysis}

Explain the decision clearly and briefly.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are Austin AI assistant."},
                    {"role": "user", "content": prompt},
                ],
            )

            result = response.choices[0].message.content

        except Exception:
            result = self._offline_reason(query, analysis)

        self.cache[key] = result

        return result
