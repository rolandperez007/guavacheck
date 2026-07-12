"""
Austin Context Builder

Builds the complete execution context for every
Austin request.
"""

from __future__ import annotations

from austin.memory import memory
from world.world_engine import world_engine

from .context import AustinContext
from .summarizer import summarizer


class ContextBuilder:

    def build(
        self,
        session_id: str,
    ) -> AustinContext:

        history = memory.recall(session_id)

        summary = summarizer.summarize(history)

        world = world_engine.dictionary(session_id)

        return AustinContext(
            session_id=session_id,
            history=history,
            summary=summary,
            world=world,
            metadata={
                "history_length": len(history),
                "language": world.get("language"),
                "currency": world.get("currency"),
                "locale": world.get("locale"),
                "timezone": world.get("timezone"),
                "region": world.get("region"),
                "unit_system": world.get("unit_system"),
            },
        )


context_builder = ContextBuilder()