from app.agents.swarm.agent_base import AgentBase


class MarketAgent(AgentBase):
    name = "market"

    async def run(self, query: str):
        q = query.lower()

        demand = 50  # baseline score

        if "lekki" in q:
            demand += 20

        if "ikeja" in q:
            demand += 15

        if "buy" in q:
            demand += 10

        if "rent" in q:
            demand += 5

        return {
            "agent": self.name,
            "demand_score": min(demand, 100),
            "trend": "rising" if demand > 60 else "stable",
            "confidence": 0.6,
        }
