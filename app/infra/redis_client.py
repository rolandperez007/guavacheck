import time
from collections import defaultdict, deque


class LocalRedis:
    """
    Temporary Redis replacement for development.
    Supports:
    - incr
    - expire simulation
    - get/set
    """

    def __init__(self):
        self.store = {}
        self.expiry = {}
        self.counters = defaultdict(int)
        self.windows = defaultdict(deque)

    def get(self, key):
        if key in self.expiry and time.time() > self.expiry[key]:
            self.store.pop(key, None)
            return None
        return self.store.get(key)

    def set(self, key, value, ex=None):
        self.store[key] = value
        if ex:
            self.expiry[key] = time.time() + ex

    def incr(self, key):
        self.counters[key] += 1
        return self.counters[key]

    def ping(self):
        return True


redis_client = LocalRedis()
