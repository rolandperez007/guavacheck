import time

class CacheService:

    def __init__(self):
        self.cache = {}

    def get(self, key):
        item = self.cache.get(key)
        if not item:
            return None

        value, expiry = item
        if time.time() > expiry:
            del self.cache[key]
            return None

        return value

    def set(self, key, value, ttl=60):
        self.cache[key] = (value, time.time() + ttl)
        cache_key = f"search:{location}"

cached = self.cache.get(cache_key)
if cached:
    return cached

result = query.execute().data
self.cache.set(cache_key, result, ttl=120)

return result