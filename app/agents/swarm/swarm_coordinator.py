from app.agents.swarm.listing_agent import ListingSwarmAgent

class SwarmCoordinator:

    def __init__(self):
        self.listing_agent = ListingSwarmAgent()

    def run(self, query):
        if "property" in query.lower() or "lekki" in query.lower():
            return {
                "agent": "listing_swarm",
                "data": self.listing_agent.run("Lekki")
            }

        return {
            "agent": "fallback",
            "data": []
        }