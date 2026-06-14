from irongate.ai.redis_client import client

BASE_SCORE = 50


def get_reputation(user_id: str) -> int:
    score = client.get(f"irongate:rep:{user_id}")

    if score is None:
        return BASE_SCORE

    return int(score)


def update_reputation(user_id: str, delta: int):
    key = f"irongate:rep:{user_id}"

    score = get_reputation(user_id)
    score = max(0, min(100, score + delta))

    client.set(key, score)
    return score
