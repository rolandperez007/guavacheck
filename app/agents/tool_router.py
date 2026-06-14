class ToolRouter:
    def __init__(self, tools=None):
        self.tools = tools or {}

    def route_full(self, query: str):
        q = query.lower().strip()

        # -------------------------
        # PROPERTY / LISTING ROUTE
        # -------------------------
        if any(
            word in q
            for word in [
                "property",
                "properties",
                "house",
                "home",
                "apartment",
                "apartments",
                "flat",
                "duplex",
                "terrace",
                "bungalow",
                "rent",
                "rental",
                "lease",
                "buy",
                "sale",
                "sell",
                "listing",
                "listings",
                "lekki",
                "ikoyi",
                "ajah",
                "sangotedo",
                "chevron",
                "victoria island",
                "vi",
            ]
        ):
            return {"route": "listing", "confidence": 0.9}

        # -------------------------
        # DEFAULT ROUTE
        # -------------------------
        return {"route": "general", "confidence": 0.5}
