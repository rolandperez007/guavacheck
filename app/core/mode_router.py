class ModeRouter:
    def route(self, intent: str):
        return {
            "property_search": "property_mode",
            "investment_analysis": "investor_mode",
            "build_analysis": "build_mode",
        }.get(intent, "general_mode")
