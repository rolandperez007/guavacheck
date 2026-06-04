from app.agents.swarm.agent_base import AgentBase


class PricingAgent(AgentBase):
    name = "pricing"

    async def run(self, query: str):

        query_lower = query.lower()

        base_price = 100000000  # default fallback (₦100M)

        multiplier = 1.0

        if "lekki" in query_lower:
            multiplier += 0.2

        if "luxury" in query_lower:
            multiplier += 0.5

        if "apartment" in query_lower:
            multiplier += 0.1

        estimated_price = int(base_price * multiplier)

        return {
            "agent": self.name,
            "estimated_price": estimated_price,
            "confidence": 0.65
        }