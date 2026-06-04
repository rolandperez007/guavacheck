from app.agents.swarm.agent_base import AgentBase


class ROIAgent(AgentBase):
    name = "roi"

    async def run(self, query: str):

        q = query.lower()

        base_roi = 8.0

        if "rent" in q:
            base_roi += 2.5

        if "lekki" in q:
            base_roi += 1.5

        if "shortlet" in q:
            base_roi += 3.0

        return {
            "agent": self.name,
            "roi_percent": round(base_roi, 2),
            "confidence": 0.7
        }