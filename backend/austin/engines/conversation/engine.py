"""
Conversation Engine
"""

from __future__ import annotations

from backend.austin.engines.base.engine import BaseEngine
from backend.austin.models.engine_result import EngineResult


class ConversationEngine(BaseEngine):
    name = "conversation"

    def execute(self, context) -> EngineResult:

        return EngineResult(
            success=True,
            engine=self.name,
            message="Conversation processed successfully.",
            metadata={
                "history": len(context.history),
            },
        )


conversation_engine = ConversationEngine()
