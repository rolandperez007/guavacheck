class AustinRouter:
    class AustinRouter:

    def should_use_gpt(self, query: str, analysis: dict):
        score = analysis.get("score", 0)

        # cheap path
        if score < 0.3:
            return False

        # expensive path
        if score > 0.7:
            return True

        # medium case
        return len(query) > 50
    
    def route(self, parsed: dict) -> dict:
        intent = parsed.get("intent", "general")
        asset = parsed.get("property_type")

        route = {
            "use_listing": False,
            "use_swarm": False,
            "use_llm": False,
            "use_pipeline": False,
            "light_mode": True,
        }

        # -------------------------
        # INVESTMENT INTELLIGENCE
        # -------------------------
        if intent in ["buy", "analyze"]:
            route["use_swarm"] = True
            route["use_llm"] = True

        # -------------------------
        # PROPERTY SEARCH MODE
        # -------------------------
        if intent == "rent" or asset:
            route["use_listing"] = True

        # -------------------------
        # FULL PROJECT MODE
        # -------------------------
        if intent == "build":
            route["use_pipeline"] = True
            route["use_swarm"] = True

        # -------------------------
        # LIGHT MODE OVERRIDE (LOW MEMORY SAFE)
        # -------------------------
        route["use_llm"] = route["use_llm"] and False  # disable heavy LLM by default

        return route
