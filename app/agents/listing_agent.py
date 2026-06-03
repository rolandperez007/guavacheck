from app.services.supabase_service import SupabaseService
from app.agents.tool_router import ToolRouter
from app.core.memory_brain import MemoryBrain


class ListingAgent:

    def __init__(self):
        self.db = SupabaseService()
        self.router = ToolRouter(tools={"listing": self.db})
        self.memory = MemoryBrain()

    async def run(self, query: str):

        user_id = "default_user"

        # 🧠 1. Save memory (Supabase)
        self.memory.remember_query(user_id, query)

        # 🧠 2. Get user preferences
        prefs = self.memory.infer_preferences(user_id)

        # ⚡ 3. AI-style tool routing
        tool_decision = self.router.route(query, memory=self.memory.infer_preferences(user_id))
        tool = tool_decision["tool"]

        # 🏠 LISTING TOOL
        if tool == "listing":

            location = None

            if query and "lekki" in query.lower():
                location = "Lekki"

            properties = self.db.search_properties(location) or []

            return {
                "tool": "listing",
                "message": "Live properties retrieved",
                "count": len(properties),
                "user_preferences": prefs,
                "routing": tool_decision,
                "results": properties
            }

        # 💰 PRICING TOOL (placeholder)
        elif tool == "pricing":
            return {
                "tool": "pricing",
                "message": "Pricing tool not implemented yet",
                "routing": tool_decision
            }

        # 📊 INSIGHT TOOL (placeholder)
        elif tool == "insight":
            return {
                "tool": "insight",
                "message": "Insight tool not implemented yet",
                "routing": tool_decision
            }

        # ❌ FALLBACK
        return {
            "tool": "fallback",
            "message": "No matching tool found",
            "routing": tool_decision
        }