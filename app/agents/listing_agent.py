from app.services.supabase_service import SupabaseService
from app.agents.tool_router import ToolRouter
from app.memory.memory_graph import MemoryGraph


class ListingAgent:

    def __init__(self):
        self.db = SupabaseService()
        self.router = ToolRouter(tools={"listing": self.db})
        self.memory = MemoryGraph()

    async def run(self, query: str, user_id: str = None):

        user_id = "default_user"

        # memory write
        self.memory.add(user_id, query)

        # AI routing (v2 brain)
        route_info = self.router.route_full(query)

        tool = route_info["tool"]

        if tool == "listing":

            location = None
            if "lekki" in query.lower():
                location = "Lekki"

            properties = self.db.search_properties(location) or []

            profile = self.memory.get_profile(user_id)

            return {
                "tool": "listing",
                "message": "AI routed listing engine",
                "routing": route_info,
                "user_profile": profile,
                "count": len(properties),
                "results": properties
            }

        return {
            "tool": tool,
            "message": "Tool executed (stub mode)",
            "routing": route_info
        }