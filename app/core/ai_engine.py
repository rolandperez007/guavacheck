from app.core.security.context import SecurityContext
from app.core.i18n.global_context import GlobalContext


class AIEngine:
    """
    Central execution engine for Austin AI system.
    Handles:
    - security enforcement
    - memory interaction
    - listing engine
    - swarm intelligence
    """

    def __init__(self, memory=None, listing_agent=None, swarm=None, events=None):
        self.memory = memory
        self.listing_agent = listing_agent
        self.swarm = swarm
        self.events = events

    # -----------------------------
    # MAIN EXECUTION PIPELINE
    # -----------------------------
    async def execute(self, query: str, context: SecurityContext):
        # 🔐 SECURITY LAYER (MANDATORY)
        if context is None:
            raise Exception("SECURITY_ERROR: Missing SecurityContext")

        self.events_emit(
            "austin.thinking",
            {"state": "start", "message": "Analyzing request...", "query": query},
        )

        # -----------------------------
        # 1. GLOBAL CONTEXT LAYER
        # -----------------------------
        global_ctx = GlobalContext.build(query)

        self.events_emit(
            "austin.thinking",
            {
                "stage": "global_context",
                "message": "Understanding global context...",
                "data": global_ctx,
            },
        )

        # -----------------------------
        # 2. MEMORY LAYER
        # -----------------------------
        await self.memory.save(context.user_id, query)

        history = await self.memory.recall(context.user_id)

        self.events_emit(
            "austin.thinking",
            {
                "stage": "memory",
                "message": "Retrieving past context...",
                "history_size": len(history),
            },
        )

        # -----------------------------
        # 3. LISTING ENGINE
        # -----------------------------
        listings = self.listing_agent.search_properties(query)

        self.events_emit(
            "austin.thinking",
            {
                "stage": "listing",
                "message": "Scanning property listings...",
                "count": len(listings) if listings else 0,
            },
        )

        # -----------------------------
        # 4. SWARM INTELLIGENCE
        # -----------------------------
        swarm_result = await self.swarm.run(query)

        score = swarm_result.get("investment_score", 0)

        # -----------------------------
        # 5. FINAL RESPONSE
        # -----------------------------
        result = {
            "query": query,
            "global_context": global_ctx,
            "memory": history,
            "listings": listings,
            "swarm": swarm_result,
            "score": score,
        }

        self.events_emit("austin.final", result)

        return result

    # -----------------------------
    # EVENT SAFETY WRAPPER
    # -----------------------------
    def events_emit(self, event_name, payload):
        if self.events:
            try:
                self.events.emit(event_name, payload)
            except Exception:
                pass
