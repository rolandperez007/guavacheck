class MemoryGraph:

    def build_profile(self, memories):
        profile = {
            "locations": [],
            "property_types": [],
            "budgets": []
        }

        for memory in memories:

            text = memory.lower()

            if "lekki" in text:
                profile["locations"].append("Lekki")

            if "duplex" in text:
                profile["property_types"].append("Duplex")

            if "apartment" in text:
                profile["property_types"].append("Apartment")

        return profile