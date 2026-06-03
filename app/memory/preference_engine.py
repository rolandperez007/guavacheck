class PreferenceEngine:

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