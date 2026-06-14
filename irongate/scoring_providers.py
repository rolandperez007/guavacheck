from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class ScorePoint:
    score: int
    reason: Optional[str] = None


def rate_limit_provider(
    context: Dict[str, any], max_requests_per_minute: int = 100
) -> Optional[ScorePoint]:
    import time

    if not hasattr(rate_limit_provider, "_req_log"):
        rate_limit_provider._req_log = {}

    user = context.get("user_id") or "anonymous"
    now = time.time()
    minute_ago = now - 60

    if user not in rate_limit_provider._req_log:
        rate_limit_provider._req_log[user] = []

    rate_limit_provider._req_log[user] = [
        ts for ts in rate_limit_provider._req_log[user] if ts > minute_ago
    ]

    if len(rate_limit_provider._req_log[user]) >= max_requests_per_minute:
        return ScorePoint(
            score=80,
            reason=f"rate limit exceeded: {len(rate_limit_provider._req_log[user])} req/min",
        )

    rate_limit_provider._req_log[user].append(now)
    return None


def duplicate_request_provider(
    context: Dict[str, any], window_seconds: int = 60
) -> Optional[ScorePoint]:
    import time
    import json

    if not hasattr(duplicate_request_provider, "_req_history"):
        duplicate_request_provider._req_history = {}

    user = context.get("user_id") or "anonymous"
    now = time.time()
    cutoff = now - window_seconds

    if user not in duplicate_request_provider._req_history:
        duplicate_request_provider._req_history[user] = []

    duplicate_request_provider._req_history[user] = [
        (ts, payload)
        for ts, payload in duplicate_request_provider._req_history[user]
        if ts > cutoff
    ]

    payload = context.get("payload") or {}
    query = context.get("query")
    if query:
        payload_key = f"query:{query}"
    elif isinstance(payload, dict):
        try:
            payload_key = json.dumps(payload, sort_keys=True)
        except Exception:
            payload_key = str(payload)
    else:
        payload_key = None

    if not payload_key:
        return None

    recent_duplicates = sum(
        1
        for ts, pk in duplicate_request_provider._req_history[user]
        if pk == payload_key
    )
    duplicate_request_provider._req_history[user].append((now, payload_key))

    if recent_duplicates >= 3:
        return ScorePoint(
            score=50,
            reason=f"duplicate request detected {recent_duplicates + 1} times in {window_seconds}s",
        )

    return None


def spam_pattern_provider(context: Dict[str, any]) -> Optional[ScorePoint]:
    """Soft score for spam patterns detected by rules."""
    return None


def automation_header_provider(context: Dict[str, any]) -> Optional[ScorePoint]:
    """Soft score for automation headers detected by rules."""
    return None


def austin_low_risk_provider(context: Dict[str, any]) -> Optional[ScorePoint]:
    """Negative score for low-risk Austin queries detected by rules."""
    return None


def payload_size_provider(context: Dict[str, any]) -> Optional[ScorePoint]:
    """Soft score for large payloads detected by rules."""
    return None
