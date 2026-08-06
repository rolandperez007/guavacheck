"""
Austin Context Builder

Builds the complete execution context for every Austin request.
"""

from __future__ import annotations

from dataclasses import asdict

from backend.world.world_engine import world_engine

from ..memory import memory
from .context import AustinContext
from .summarizer import summarizer


class ContextBuilder:
    def build(
        self,
        session_id: str,
        query: str = "",
    ) -> AustinContext:

        history = memory.recall(session_id)

        summary = summarizer.summarize(history)

        world = world_engine.build(
            query=query,
            country="NG",
            language="en",
        )

        return AustinContext(
            session_id=session_id,
            history=history,
            summary=summary,
            world=asdict(world),
            metadata={
                "history_length": len(history),
                "language": world.language,
                "currency": world.currency,
                "country": world.country,
            },
        )


context_builder = ContextBuilder()
