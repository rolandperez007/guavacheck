class PreferenceEngine:
    def __init__(self):
        self.store = {}

    def log_interaction(self, user_id, query):
        if user_id not in self.store:
            self.store[user_id] = []

        self.store[user_id].append({
            "query": query
        })

    def build_profile(self, user_id):
        data = self.store.get(user_id, [])

        locations = []
        keywords = []

        for item in data:
            q = item["query"].lower()

            if "lekki" in q:
                locations.append("Lekki")

            keywords.extend(q.split())

        return {
            "locations": list(set(locations)),
            "keywords": list(set(keywords))
        }

    def build_preferences(self, memory_records):

        locations = []
        keywords = []

        for row in memory_records:

            query = row.get("query", "").lower()

            if "lekki" in query:
                locations.append("Lekki")

            if "ikoyi" in query:
                locations.append("Ikoyi")

            if "terrace" in query:
                keywords.append("Terrace")

            if "detached" in query:
                keywords.append("Detached")

        return {
            "locations": list(set(locations)),
            "keywords": list(set(keywords))
        }