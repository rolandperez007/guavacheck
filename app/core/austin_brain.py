class AustinBrain:
    def analyze(self, parsed: dict):
        intent = parsed.get("intent", "general")
        location = parsed.get("location")
        price = parsed.get("financial", {}).get("price")
        currency = parsed.get("financial", {}).get("currency", "USD")
        property_type = parsed.get("property_type")

        score = 0.5

        if intent == "buy":
            score += 0.2
        elif intent == "analyze":
            score += 0.25
        elif intent == "sell":
            score -= 0.1

        hot_markets = ["Lekki", "London", "Dubai", "New York", "Toronto"]

        if location:
            if any(hot in location for hot in hot_markets):
                score += 0.2
            else:
                score += 0.05

        if price:
            if price < 50_000:
                score += 0.1
            elif price > 500_000_000:
                score -= 0.1

        if property_type == "luxury":
            score += 0.1
        elif property_type == "shared":
            score += 0.05

        if score >= 0.75:
            decision = "strong_buy"
        elif score >= 0.6:
            decision = "buy"
        elif score >= 0.45:
            decision = "hold"
        else:
            decision = "avoid"

        return {"decision": decision, "score": round(score, 2), "currency": currency}

    # IMPORTANT: FIXED INDENTATION HERE
    def explain(self, result: dict, query: str):
        decision = result["decision"]
        score = result["score"]

        if decision == "strong_buy":
            return f"Strong investment signal 📈 (score {score}). High potential opportunity."

        if decision == "buy":
            return f"Good opportunity 👍 (score {score}). Worth considering."

        if decision == "hold":
            return f"Neutral market ⚖️ (score {score}). Wait for better signals."

        return f"High risk ⚠️ (score {score}). Not recommended."
