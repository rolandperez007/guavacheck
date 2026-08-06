from app.infra.redis_client import redis_client
from irongate.distributed.state_store import state_store


def distributed_rate_limit_rule(context):
    user_id = context.get("user_id")
    if not user_id:
        return True

    count = state_store.increment_rate(user_id, window_sec=60)

    if count > 100:
        return "distributed rate limit exceeded"

    return True


def distributed_duplicate_detection_rule(context):
    user_id = context.get("user_id")
    payload = context.get("payload", {})

    fingerprint = state_store.fingerprint(payload)
    key = f"{user_id}:{fingerprint}"

    count = state_store.add_request(key, window_sec=60)

    if count > 3:
        return "duplicate request detected across distributed layer"

    return True


import time


def distributed_rate_limit_rule(context):
    user_id = context.get("user_id")
    if not user_id:
        return True

    key = f"rate:{user_id}"
    count = redis_client.incr(key)

    if count == 1:
        redis_client.set(key, 1, ex=60)

    if count > 100:
        return "rate limit exceeded (distributed rule)"

    return True


def block_empty_payload(context):
    if not context.get("payload"):
        return "Empty payload"
    return True


def allow_only_known_actions(context):
    allowed = ["run_job", "ws_message", "api_call"]
    if context.get("action") not in allowed:
        return f"Unknown action: {context.get('action')}"
    return True


def block_suspicious_users(context):
    banned_users = ["test_spam_user"]
    if context.get("user_id") in banned_users:
        return "User is banned"
    return True


def spam_pattern_rule(context):
    payload = context.get("payload") or {}
    text = ""
    if isinstance(payload, dict):
        text = " ".join(str(v) for v in payload.values() if isinstance(v, str))
    text = text.lower()
    spam_indicators = ["buy now", "free", "click here", "subscribe", "cheap"]
    for phrase in spam_indicators:
        if phrase in text:
            return f"spam pattern detected: {phrase}"
    return True


def automation_header_rule(context):
    headers = context.get("headers") or {}
    ua = headers.get("user-agent", "").lower()
    if "bot" in ua or "curl" in ua or "wget" in ua:
        return "automation user-agent detected"
    if headers.get("x-automation") in ("1", "true"):
        return "custom automation header detected"
    return True


def austin_low_risk_rule(context):
    q = context.get("query") or ""
    if not q:
        payload = context.get("payload") or {}
        if isinstance(payload, dict):
            q = payload.get("query") or payload.get("message") or ""
    q = (q or "").lower()
    low_risk_phrases = ["build house", "quote", "estimate", "calculate mortgage"]
    for phrase in low_risk_phrases:
        if phrase in q:
            return "austin low-risk query detected"
    return True


def payload_size_limit_rule(context, max_bytes: int = 1024 * 100):
    import json

    payload = context.get("payload") or {}
    if not isinstance(payload, dict):
        return True
    try:
        size = len(json.dumps(payload).encode("utf-8"))
    except Exception:
        return "unable to calculate payload size"
    if size > max_bytes:
        return f"payload too large: {size} bytes"
    return True


def rate_limit_rule(context, max_requests_per_minute: int = 100):
    """Simple in-memory rate limiting as a soft risk rule."""

    if not hasattr(rate_limit_rule, "_req_log"):
        rate_limit_rule._req_log = {}

    user = context.get("user_id") or "anonymous"
    now = time.time()
    minute_ago = now - 60

    if user not in rate_limit_rule._req_log:
        rate_limit_rule._req_log[user] = []

    rate_limit_rule._req_log[user] = [
        ts for ts in rate_limit_rule._req_log[user] if ts > minute_ago
    ]

    recent_count = len(rate_limit_rule._req_log[user])

    if recent_count >= max_requests_per_minute:
        return f"rate limit: {recent_count} requests/min >= {max_requests_per_minute}"

    rate_limit_rule._req_log[user].append(now)
    return True


def duplicate_request_rule(context, window_seconds: int = 60):
    """Detect repeated identical requests as a soft risk rule."""
    import json

    if not hasattr(duplicate_request_rule, "_req_history"):
        duplicate_request_rule._req_history = {}

    user = context.get("user_id") or "anonymous"
    now = time.time()
    cutoff = now - window_seconds

    if user not in duplicate_request_rule._req_history:
        duplicate_request_rule._req_history[user] = []

    duplicate_request_rule._req_history[user] = [
        (ts, payload)
        for ts, payload in duplicate_request_rule._req_history[user]
        if ts > cutoff
    ]

    payload_key = None
    payload = context.get("payload") or {}
    query = context.get("query")

    if query:
        payload_key = f"query:{query}"
    elif isinstance(payload, dict):
        try:
            payload_key = json.dumps(payload, sort_keys=True)
        except Exception:
            payload_key = str(payload)

    if payload_key:
        recent_duplicates = sum(
            1
            for ts, pk in duplicate_request_rule._req_history[user]
            if pk == payload_key
        )

        if recent_duplicates >= 3:
            return f"duplicate request detected {recent_duplicates} times in {window_seconds}s"

        duplicate_request_rule._req_history[user].append((now, payload_key))

    return True
