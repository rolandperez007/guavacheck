from app.agents.listing_agent import ListingAgent
from app.services.supabase_service import SupabaseService
from app.core.tool_router import ToolRouter
class AustinEngine:

    def __init__(self):
        self.router = ToolRouter()
        self.services = {
            "supabase": SupabaseService()
        }

        self.agents = {
            "listing": ListingAgent(self.services)
        }

    async def run(self, query: str):

    # STEP 1: tool execution layer
    tool_result = self.router.execute(query)

    # STEP 2: keep compatibility layer (important for now)
    return {
        "query": query,
        "tool_output": tool_result
    }

class AustinEngine:

    def __init__(self):
        self.last_call = 0

    async def run(self, query: str):

        if time.time() - self.last_call < 1:
            return {"error": "Rate limit active"}

        self.last_call = time.time()
        from app.agents.listing_agent import ListingAgent
from app.core.swarm_coordinator import SwarmCoordinator
from app.services.supabase_service import SupabaseService

class AustinEngine:

    def __init__(self):

        services = {
            "supabase": SupabaseService()
        }

        self.swarm = SwarmCoordinator({
            "listing": ListingAgent(services),
            # "pricing": PricingAgent(services),
            # "insight": InsightAgent(services),
        })

    async def run(self, query: str):
        return await self.swarm.run(query)