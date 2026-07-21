"""
Austin Router

Receives incoming requests, builds global execution context,
stores conversation memory, publishes events, queues work,
and immediately acknowledges the request.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from uuid import uuid4

from .context import context_manager
from .events import events
from .memory import memory
from .queue import queue

from backend.world.world_engine import world_engine


@dataclass(slots=True)
class RouterResult:
    intent: str
    confidence: float
    engine: str
    response: str
    job_id: str
    correlation_id: str
    trace_id: str
    timestamp: str


class AustinRouter:

    def route(
        self,
        *,
        session_id: str,
        message: str,
    ) -> RouterResult:

        correlation_id = str(uuid4())
        trace_id = str(uuid4())

        timestamp = datetime.now(timezone.utc).isoformat()

        intent = "chat"
        confidence = 0.95

        # ----------------------------------------------------------
        # Build World Context
        # ----------------------------------------------------------

        world = world_engine.build(
            query=message,
            country="NG",
            language="en",
        )

        context_manager.set(
            session_id,
            "world",
            world,
        )

        # ----------------------------------------------------------
        # Save Memory
        # ----------------------------------------------------------

        memory.save(
            {
                "id": f"{session_id}:{memory.count()}",
                "user_id": session_id,
                "category": "conversation",
                "title": "chat",
                "value": message,
            }
        )

        # ----------------------------------------------------------
        # Queue Background Work
        # ----------------------------------------------------------

        job = queue.enqueue(
            payload={
                "session_id": session_id,
                "message": message,
                "world": world,
            },
            correlation_id=correlation_id,
        )

        # ----------------------------------------------------------
        # Publish Event
        # ----------------------------------------------------------

        events.publish(
            "AustinChatReceived",
            {
                "correlation_id": correlation_id,
                "engine": "austin",
                "source_service": "austin.router",
                "severity": "info",
                "category": "conversation",
                "message": f"Austin accepted request for {session_id}",
                "metadata": {
                    "intent": intent,
                    "country": world.country,
                    "language": world.language,
                    "currency": world.currency,
                },
            },
        )

        # ----------------------------------------------------------
        # Immediate Response
        # ----------------------------------------------------------

        return RouterResult(
            intent=intent,
            confidence=confidence,
            engine="austin",
            response="Austin has accepted your request and is processing it in the background.",
            job_id=job.job_id,
            correlation_id=correlation_id,
            trace_id=trace_id,
            timestamp=timestamp,
        )


router = AustinRouter()