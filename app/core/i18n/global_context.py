class GlobalContext:
    """
    Lightweight global context for i18n + geo fallback.
    """

    COUNTRY_CURRENCY_MAP = {
        "NG": "NGN",
        "US": "USD",
        "GB": "GBP",
        "EU": "EUR",
        "KE": "KES",
        "GH": "GHS",
        "ZA": "ZAR",
    }

    COUNTRY_LANGUAGE_MAP = {
        "NG": "en",
        "US": "en",
        "GB": "en",
        "FR": "fr",
        "DE": "de",
        "ES": "es",
    }

    @staticmethod
    def build(query: str) -> dict:
        query_lower = query.lower()

        country = "NG"

        if any(x in query_lower for x in ["dollar", "usd", "usa", "new york"]):
            country = "US"

        elif any(x in query_lower for x in ["london", "uk", "pound"]):
            country = "GB"

        elif any(x in query_lower for x in ["euro", "france", "germany"]):
            country = "EU"

        currency = GlobalContext.COUNTRY_CURRENCY_MAP.get(country, "NGN")
        language = GlobalContext.COUNTRY_LANGUAGE_MAP.get(country, "en")

        return {
            "country": country,
            "currency": currency,
            "language": language,
            "query": query,
        }
