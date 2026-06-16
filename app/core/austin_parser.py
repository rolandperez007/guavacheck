import re

class AustinParser:

    def parse(self, text: str):
        text_lower = text.lower()

        # -------------------------
        # INTENT DETECTION
        # -------------------------
        if any(word in text_lower for word in ["buy", "purchase", "invest"]):
            intent = "buy"
        elif "sell" in text_lower:
            intent = "sell"
        elif "analyze" in text_lower or "good deal" in text_lower:
            intent = "analyze"
        else:
            intent = "general"

        # -------------------------
        # LOCATION DETECTION (simple pattern + keywords)
        # -------------------------
        locations = ["lekki", "lagos", "dubai", "london", "new york", "toronto"]
        location = next((loc for loc in locations if loc in text_lower), None)

        # -------------------------
        # PRICE EXTRACTION (VERY IMPORTANT)
        # -------------------------
        price_match = re.search(r"(\d[\d,]*)\s*(usd|ngn|million|m|k)?", text_lower)

        price = None
        currency = "USD"

        if price_match:
            raw = price_match.group(1).replace(",", "")
            price = int(raw)

        # -------------------------
        # PROPERTY TYPE
        # -------------------------
        property_type = None
        if "luxury" in text_lower:
            property_type = "luxury"
        elif "shared" in text_lower or "apartment" in text_lower:
            property_type = "shared"
        elif "house" in text_lower:
            property_type = "house"

        return {
            "intent": intent,
            "location": location,
            "financial": {
                "price": price,
                "currency": currency
            },
            "property_type": property_type
        }