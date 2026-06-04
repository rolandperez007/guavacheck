from app.agents.swarm.pricing_agent import PricingAgent
from app.agents.swarm.roi_agent import ROIAgent
from app.agents.swarm.market_agent import MarketAgent


class SwarmCoordinatorV2:

    def __init__(self):

        self.agents = {
            "pricing": PricingAgent(),
            "roi": ROIAgent(),
            "market": MarketAgent()
        }

    async def run(self, query: str):

        results = {}

        for name, agent in self.agents.items():
            results[name] = await agent.run(query)

        # decision logic
        pricing = results["pricing"]
        roi = results["roi"]
        market = results["market"]

        investment_score = (
            pricing["confidence"] * 0.3 +
            roi["confidence"] * 0.4 +
            market["confidence"] * 0.3
        )

        return {
            "swarm": "v1",
            "investment_score": round(investment_score, 2),
            "recommendation": "strong buy" if investment_score > 0.7 else "hold",
            "breakdown": results
        }