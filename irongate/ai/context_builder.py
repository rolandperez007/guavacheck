import time

# in-memory lightweight tracker (replace with Redis later)
from irongate.ai.redis_client import client
from irongate.ai.reputation import get_reputation


def build_ai_context(context: dict):
    user_id = context.get("user_id")
    endpoint = context.get("path", "unknown")
    now = time.time()

    key = f"irongate:req:{user_id}"

    client.zadd(key, {str(now): now})
    client.zremrangebyscore(key, 0, now - 60)

    request_rate = client.zcard(key)

    reputation = get_reputation(user_id)

    return {
        "user_id": user_id,
        "endpoint": endpoint,
        "request_rate_per_min": request_rate,
        "has_auth": bool(context.get("headers", {}).get("authorization")),
        "reputation": reputation,
    }


def build_ai_context(context: dict):
    user_id = context.get("user_id")
    endpoint = context.get("path", "unknown")

    now = time.time()

    key = f"irongate:req:{user_id}"

    # store timestamp
    client.zadd(key, {str(now): now})

    # remove entries older than 60 seconds
    client.zremrangebyscore(key, 0, now - 60)

    # count requests in last minute
    request_rate = client.zcard(key)

    return {
        "user_id": user_id,
        "endpoint": endpoint,
        "request_rate_per_min": request_rate,
        "has_auth": bool(context.get("headers", {}).get("authorization")),
    }


def compute_risk(ai_context: dict):
    score = 0

    if not ai_context["has_auth"]:
        score += 60

    if ai_context["request_rate_per_min"] > 20:
        score += 35
    elif ai_context["request_rate_per_min"] > 10:
        score += 15

    if "admin" in ai_context["endpoint"]:
        score += 20

    return min(score, 100)


try:
    client.zadd(key, {str(now): now})
    client.zremrangebyscore(key, 0, now - 60)
    request_rate = client.zcard(key)
except Exception:
    request_rate = 1


def build_ai_context(context: dict):
    user_id = context.get("user_id")
    endpoint = context.get("path", "unknown")

    now = time.time()

    # log request
    REQUEST_LOG[user_id].append(now)

    # keep last 1 minute only
    REQUEST_LOG[user_id] = [t for t in REQUEST_LOG[user_id] if now - t < 60]

    request_rate = len(REQUEST_LOG[user_id])

    return {
        "user_id": user_id,
        "endpoint": endpoint,
        "request_rate_per_min": request_rate,
        "has_auth": bool(context.get("headers", {}).get("authorization")),
    }


def build_ai_context(context: dict):
    user_id = context.get("user_id")
    endpoint = context.get("path", "unknown")
    now = time.time()

    key = f"irongate:req:{user_id}"

    client.zadd(key, {str(now): now})
    client.zremrangebyscore(key, 0, now - 60)

    request_rate = client.zcard(key)

    reputation = get_reputation(user_id)

    return {
        "user_id": user_id,
        "endpoint": endpoint,
        "request_rate_per_min": request_rate,
        "has_auth": bool(context.get("headers", {}).get("authorization")),
        "reputation": reputation,
    }
