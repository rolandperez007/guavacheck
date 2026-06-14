class ProjectClassifier:
    ASSET_TYPES = {
        "residential": [
            "house",
            "apartment",
            "villa",
            "estate",
            "duplex",
            "terrace",
            "condo",
        ],
        "hospitality": ["hotel", "resort", "short let", "serviced apartment"],
        "healthcare": ["hospital", "clinic", "medical center", "diagnostic center"],
        "education": ["school", "college", "university", "training center"],
        "industrial": ["factory", "warehouse", "manufacturing plant", "data center"],
        "commercial": ["office", "mall", "shopping center", "retail plaza"],
        "infrastructure": [
            "airport",
            "rail station",
            "bus terminal",
            "government building",
        ],
    }

    @staticmethod
    def classify(query: str):
        text = query.lower()

        for category, keywords in ProjectClassifier.ASSET_TYPES.items():
            for keyword in keywords:
                if keyword in text:
                    return {"category": category, "asset_type": keyword}

        return {"category": "general", "asset_type": None}
