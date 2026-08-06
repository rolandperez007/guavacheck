class FakeRedis:
    """
    Temporary fallback so system runs without Redis installed.
    DO NOT use in production.
    """

    def __init__(self):
        self.store = {}

    def ping(self):
        return True

    def set(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key)

    def lpush(self, key, value):
        self.store.setdefault(key, []).insert(0, value)

    def rpop(self, key):
        if self.store.get(key):
            return self.store[key].pop()
        return None
