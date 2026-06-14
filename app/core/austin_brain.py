class AustinBrain:
    def analyze(self, parsed: dict):
        intent = parsed.get("intent", "general")
        location = parsed.get("location")
        price = parsed.get("financial", {}).get("price")
        currency = parsed.get("financial", {}).get("currency", "USD")
        property_type = parsed.get("property_type")

        score = 0.5  # base neutral score

        # -------------------------
        # INTENT BOOSTS
        # -------------------------
        if intent == "buy":
            score += 0.2
        elif intent == "analyze":
            score += 0.25
        elif intent == "sell":
            score -= 0.1

        # -------------------------
        # LOCATION LOGIC (GLOBAL REAL ESTATE SIGNAL)
        # -------------------------
        hot_markets = ["Lekki", "London", "Dubai", "New York", "Toronto"]

        if location:
            if any(hot in location for hot in hot_markets):
                score += 0.2
            else:
                score += 0.05

        # -------------------------
        # PRICE LOGIC (AFFORDABILITY HEURISTIC)
        # -------------------------
        if price:
            if price < 50_000:
                score += 0.1
            elif price > 500_000_000:
                score -= 0.1

        # -------------------------
        # PROPERTY TYPE LOGIC
        # -------------------------
        if property_type == "luxury":
            score += 0.1
        elif property_type == "shared":
            score += 0.05

        # -------------------------
        # FINAL DECISION
        # -------------------------
        if score >= 0.75:
            decision = "strong_buy"
        elif score >= 0.6:
            decision = "buy"
        elif score >= 0.45:
            decision = "hold"
        else:
            decision = "avoid"

        return {"decision": decision, "score": round(score, 2), "currency": currency}
