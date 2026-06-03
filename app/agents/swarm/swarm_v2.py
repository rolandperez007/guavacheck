from app.agents.swarm.listing_agent import ListingSwarmAgent


class SwarmV2:

    def __init__(self):
        self.listing = ListingSwarmAgent()

    def run(self, query, tool_decision=None):
        tool = tool_decision.get("tool") if tool_decision else "listing"

        if tool == "listing":
            return {
                "agent": "listing_v2",
                "data": self.listing.run(self._extract_location(query))
            }

        if tool == "pricing":
            return {
                "agent": "pricing_v2",
                "data": {"message": "pricing agent ready (stub)"}
            }

        if tool == "insight":
            return {
                "agent": "insight_v2",
                "data": {"message": "insight agent ready (stub)"}
            }

        return {
            "agent": "fallback",
            "data": []
        }

    def _extract_location(self, query):
        q = query.lower()
        if "lekki" in q:
            return "Lekki"
        if "ajah" in q:
            return "Ajah"
        return None