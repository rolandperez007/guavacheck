try:
    import redis

    redis_client = redis.Redis(host="localhost", port=6379, db=0)
    redis_client.ping()

except Exception:
    from app.core.jobs.local_redis_fallback import FakeRedis

    redis_client = FakeRedis()
