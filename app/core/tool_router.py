from app.tools.property_tools import PropertyTools


class ToolRouter:

    def __init__(self):
        self.property_tools = PropertyTools()

    def route(self, query: str):

        query_lower = query.lower()

        tools = []

        # 🏠 LISTINGS
        if any(word in query_lower for word in ["property", "house", "apartment", "lekki", "rent", "buy"]):
            tools.append("listing")

        # 💰 PRICING
        if any(word in query_lower for word in ["price", "cost", "worth", "valuation"]):
            tools.append("pricing")

      class ToolRouter:

    def __init__(self, supabase_service):
        self.db = supabase_service

    def route(self, query: str):
        q = query.lower()

        if "price" in q or "cost" in q:
            return "pricing_tool"

        if "rent" in q or "buy" in q or "lekki" in q:
            return "listing_tool"

        if "insight" in q or "market" in q:
            return "insight_tool"

        return "listing_tool"