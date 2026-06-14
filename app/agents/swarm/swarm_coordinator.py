from app.agents.listing_agent import ListingAgent
from app.core.security.context import SecurityContext


class SwarmCoordinator:
    def __init__(self):
        self.listing_agent = ListingAgent()

    # -----------------------------
    # MAIN ENTRY (SECURE)
    # -----------------------------
    async def run(self, query: str, context: SecurityContext):
        # 🧠 ROUTING DECISION (simple initial logic)
        routing = self._route(query)

        if routing == "property_search":
            result = await self.listing_agent.run(query=query, context=context)
        else:
            result = {"message": "No matching agent route", "query": query}

        return {"routing": routing, "result": result}

    # -----------------------------
    # SIMPLE ROUTER LOGIC
    # -----------------------------
    def _route(self, query: str) -> str:
        q = query.lower()

        if any(word in q for word in ["house", "apartment", "rent", "buy", "property"]):
            return "property_search"

        return "unknown"
