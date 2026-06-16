import redis
import json
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

r = redis.Redis.from_url(REDIS_URL, decode_responses=True)


class Cache:

    @staticmethod
    def get(key: str):
        value = r.get(key)
        return json.loads(value) if value else None

    @staticmethod
    def set(key: str, value, ttl=3600):
        r.setex(key, ttl, json.dumps(value))