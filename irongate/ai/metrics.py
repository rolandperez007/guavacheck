from irongate.ai.redis_client import client


def get_user_metrics(user_id: str):
    rep = client.get(f"irongate:rep:{user_id}") or 50

    req_key = f"irongate:req:{user_id}"
    req_count = client.zcard(req_key)

    history_key = f"irongate:history:{user_id}"
    history = client.lrange(history_key, 0, 10)

    return {
        "user_id": user_id,
        "reputation_score": int(rep),
        "requests_last_min": req_count,
        "recent_behavior": list(history),
        "status_band": (
            "trusted" if int(rep) >= 80 else "normal" if int(rep) >= 50 else "risky"
        ),
    }
