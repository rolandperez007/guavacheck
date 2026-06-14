import re
from collections import Counter


class QueryParser:
    INTENTS = {
        "buy": ["buy", "purchase", "invest", "investment", "should i buy", "worth it"],
        "rent": ["rent", "lease", "let", "airbnb", "shortlet"],
        "sell": ["sell", "list", "offload"],
        "analyze": ["roi", "return", "profit", "analysis"],
    }

    PROPERTY_TYPES = {
        "apartment": ["apartment", "flat", "condo", "unit"],
        "house": ["house", "home", "detached"],
        "luxury": ["villa", "penthouse", "mansion", "luxury"],
        "shared": ["studio", "miniflat", "room"],
    }

    LOCATION_PATTERNS = [
        r"in\s([a-zA-Z\s,]+)",
        r"at\s([a-zA-Z\s,]+)",
        r"near\s([a-zA-Z\s,]+)",
    ]

    CURRENCY_SYMBOLS = {
        "$": "USD",
        "€": "EUR",
        "£": "GBP",
        "₦": "NGN",
        "¥": "JPY",
        "₹": "INR",
    }

    GLOBAL_COUNTRY_HINTS = {
        "nigeria": "NG",
        "usa": "US",
        "uk": "GB",
        "london": "GB",
        "lagos": "NG",
        "dubai": "AE",
        "canada": "CA",
    }

    @staticmethod
    def parse(query: str):
        text = query.lower()

        # -------------------------
        # INTENT SCORING
        # -------------------------
        intent_scores = Counter()

        for intent, phrases in QueryParser.INTENTS.items():
            for phrase in phrases:
                if phrase in text:
                    intent_scores[intent] += 1

        intent = intent_scores.most_common(1)[0][0] if intent_scores else "general"

        # -------------------------
        # LOCATION
        # -------------------------
        location = None
        for pattern in QueryParser.LOCATION_PATTERNS:
            match = re.search(pattern, text)
            if match:
                location = match.group(1).strip().title()
                break

        # -------------------------
        # COUNTRY
        # -------------------------
        country = None
        for k, v in QueryParser.GLOBAL_COUNTRY_HINTS.items():
            if k in text:
                country = v
                break

        # -------------------------
        # PROPERTY TYPE
        # -------------------------
        property_type = None
        for ptype, keywords in QueryParser.PROPERTY_TYPES.items():
            for kw in keywords:
                if kw in text:
                    property_type = ptype
                    break

        # -------------------------
        # PRICE EXTRACTION
        # -------------------------
        price = None
        match = re.search(r"(\d+(\.\d+)?\s?(k|m|million|billion)?)", text)

        if match:
            raw = match.group(0).replace(",", "").lower()

            if "k" in raw:
                price = float(raw.replace("k", "")) * 1_000
            elif "m" in raw or "million" in raw:
                price = float(raw.replace("m", "").replace("million", "")) * 1_000_000
            elif "b" in raw:
                price = (
                    float(raw.replace("b", "").replace("billion", "")) * 1_000_000_000
                )
            else:
                try:
                    price = float(raw)
                except:
                    price = None

        # -------------------------
        # CURRENCY
        # -------------------------
        currency = next(
            (
                code
                for sym, code in QueryParser.CURRENCY_SYMBOLS.items()
                if sym in query
            ),
            "USD",
        )

        # -------------------------
        # KEYWORDS
        # -------------------------
        words = re.findall(r"[a-zA-Z]+", text)
        stopwords = {"the", "is", "in", "at", "to", "a", "of", "and", "for"}
        keywords = [w for w in words if w not in stopwords and len(w) > 2]

        # -------------------------
        # ROUTING SIGNAL
        # -------------------------
        routing = {
            "is_investment": intent in ["buy", "analyze"],
            "has_location": location is not None,
            "has_price": price is not None,
            "is_property_query": property_type is not None,
        }

        return {
            "query": query,
            "intent": intent,
            "location": location,
            "country": country,
            "property_type": property_type,
            "financial": {"price": price, "currency": currency},
            "keywords": keywords,
            "routing": routing,
            "confidence": {
                "intent": 0.8 if intent != "general" else 0.3,
                "location": 0.6 if location else 0.0,
                "price": 0.7 if price else 0.0,
            },
            "meta": {"version": "global_parser_v3"},
        }
