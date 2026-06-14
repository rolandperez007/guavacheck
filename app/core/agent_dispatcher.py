# app/core/agent_dispatcher.py

from app.agents.listing_agent import ListingAgent
from app.agents.mortgage_agent import MortgageAgent


class AgentDispatcher:
    def __init__(self):
        self.agents = {
            "property_search": ListingAgent(),
            "mortgage": MortgageAgent(),
        }

    async def dispatch(self, intent, query):
        agent = self.agents.get(intent)

        if not agent:
            return {"message": "No matching agent"}

        return await agent.run(query)


from app.core.tool_router import ToolRouter
