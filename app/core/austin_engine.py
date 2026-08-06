import asyncio

from app.agents.listing_agent import ListingAgent
from app.agents.swarm.swarm_coordinator_v2 import SwarmCoordinatorV2
from app.core.events.event_bus import EventBus
from app.core.i18n.global_context import GlobalContext
from app.core.memory.hybrid_memory import HybridMemory
from app.core.project_classifier import ProjectClassifier
from app.core.query_parser import QueryParser
from app.core.router.model_gateway import ModelGatewayV2
from app.core.security.context import SecurityContext
from app.core.ui.ui_event_stream import UIEventStream


class AustinEngine:
    def __init__(self):
        self.listing_agent = ListingAgent()
        self.swarm = SwarmCoordinatorV2()
        self.memory = HybridMemory()
        self.events = EventBus()
        self.ui = UIEventStream()
        self.gateway = ModelGatewayV2()

    def _recommend(self, score: float) -> str:
        if score >= 0.75:
            return "buy"
        if score >= 0.5:
            return "hold"
        return "avoid"

    async def execute(self, query: str, context: SecurityContext):
        if not context:
            raise Exception("SecurityContext required")

        self.events.emit(
            "austin.thinking",
            {"state": "start", "message": "Analyzing request...", "query": query},
        )

        global_ctx = GlobalContext.build(query)
        parsed = QueryParser.parse(query)
        project = ProjectClassifier.classify(query)

        await self.memory.save(context.user_id, query)
        history = await self.memory.recall(context.user_id)

        listing_result = await self.listing_agent.run(query=query)
        swarm_result = await self.swarm.run(query)

        score = swarm_result.get("investment_score", 0)

        decision = {
            "mode": "austin_v3",
            "recommendation": self._recommend(score),
            "confidence": score,
            "global_context": global_ctx,
        }

        llm_prompt = f"""
You are Austin AI Engine.

GLOBAL CONTEXT:
{global_ctx}

PARSED:
{parsed}

PROJECT:
{project}

SCORE:
{score}

QUERY:
{query}

Return structured reasoning.
"""

        try:
            llm_result = await self.gateway.ask(llm_prompt)
        except Exception as e:
            llm_result = {"fallback": True, "error": str(e)}

        self.events.emit(
            "austin.complete", {"message": "Execution complete", "query": query}
        )

        return {
            "query": query,
            "user_id": context.user_id,
            "org_id": context.org_id,
            "global_context": global_ctx,
            "parsed": parsed,
            "project": project,
            "memory_size": len(history),
            "listing": listing_result,
            "swarm": swarm_result,
            "decision": decision,
            "ai_response": llm_result,
        }

    async def stream_execute(self, query: str, context: SecurityContext):
        yield {"type": "thinking", "stage": "start", "message": "Analyzing request..."}

        await asyncio.sleep(0.2)

        global_ctx = GlobalContext.build(query)

        yield {"type": "context", "data": global_ctx}
