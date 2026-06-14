class MemoryGraph:
    def __init__(self):
        self.store = {}

    def add(self, user_id: str, query: str):
        self.store.setdefault(user_id, [])
        self.store[user_id].append(query)

    def get_profile(self, user_id: str):
        queries = self.store.get(user_id, [])

        return {
            "total_queries": len(queries),
            "locations": list({q for q in queries if isinstance(q, str)}),
            "keywords": queries[-5:],
        }
