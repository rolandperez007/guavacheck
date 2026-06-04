class MemoryGraph:
    """
    Simple graph memory layer for Austin agents
    Stores interactions + builds lightweight user profile graph
    """

    def __init__(self):
        self.store = {}

    # ✅ FIX: this replaces missing .add()
    def add(self, user_id: str, query: str):
        if user_id not in self.store:
            self.store[user_id] = {
                "queries": [],
                "locations": [],
                "keywords": []
            }

        self.store[user_id]["queries"].append(query)

        q = query.lower()

        # simple extraction logic
        if "lekki" in q:
            self.store[user_id]["locations"].append("Lekki")

        self.store[user_id]["keywords"].extend(q.split())

    def get_profile(self, user_id: str):
        data = self.store.get(user_id, {
            "queries": [],
            "locations": [],
            "keywords": []
        })

        return {
            "total_queries": len(data["queries"]),
            "locations": list(set(data["locations"])),
            "keywords": list(set(data["keywords"]))[:20]
        }