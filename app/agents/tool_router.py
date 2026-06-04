class ToolRouter:
    """
    Austin AI Tool Router

    Decides which engine/tool should handle a user query.
    Returns routing metadata for transparency and debugging.
    """

    def __init__(self, tools=None):
        self.tools = tools or {}

    def route_full(self, query: str):
        q = query.lower().strip()

        # PROPERTY / LISTING SEARCH
        if any(word in q for word in [
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
            "vi"
        ]):
            return {
                "tool": "listing",
                "confidence": 0.95,
                "reason": "property search detected"
            }

        # ROI / INVESTMENT ANALYSIS
        if any(word in q for word in [
            "roi",
            "return on investment",
            "yield",
            "cashflow",
            "cash flow",
            "profitability",
            "investment score",
            "analyze investment"
        ]):
            return {
                "tool": "roi",
                "confidence": 0.90,
                "reason": "investment analysis detected"
            }

        # MORTGAGE CALCULATIONS
        if any(word in q for word in [
            "mortgage",
            "monthly payment",
            "loan",
            "interest rate",
            "amortization"
        ]):
            return {
                "tool": "mortgage",
                "confidence": 0.92,
                "reason": "mortgage query detected"
            }

        # MARKET ANALYSIS
        if any(word in q for word in [
            "market",
            "trend",
            "price trend",
            "market report",
            "appreciation",
            "forecast"
        ]):
            return {
                "tool": "market",
                "confidence": 0.88,
                "reason": "market analysis detected"
            }

        # DEFAULT FALLBACK
        return {
            "tool": "listing",
            "confidence": 0.30,
            "reason": "fallback default route"
        }

    def execute(self, query: str):
        """
        Compatibility method for older code.
        """
        return self.route_full(query)