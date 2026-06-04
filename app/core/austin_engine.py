from app.agents.swarm.swarm_coordinator_v2 import SwarmCoordinatorV2
from app.agents.listing_agent import ListingAgent


class AustinEngine:

    def __init__(self):

        # core swarm brain
        self.swarm = SwarmCoordinatorV2()

        # listing brain (separate for retrieval)
        self.listing_agent = ListingAgent()

    async def execute(self, query: str, user_id: str = None):

        # 1. Run listing retrieval
        listing_result = await self.listing_agent.run(
            query=query,
            user_id=user_id
        )

        # 2. Run swarm intelligence
        swarm_result = await self.swarm.run(query)

        # 3. Merge intelligence layers
        return {
            "tool": "austin",
            "query": query,
            "listing": listing_result,
            "swarm": swarm_result,
            "decision_layer": {
                "mode": "swarm_fusion",
                "confidence": swarm_result.get("investment_score", 0)
            }
        }