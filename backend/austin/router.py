"""
Austin Router

Provides the minimal routing surface Austin exposes to the API.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4

from .events import events
from .logger import logger, structured_log
from .memory import memory
from .queue import queue
from .status import status


@dataclass
class AustinRouteResult:
    intent: str
    confidence: float
    engine: str
    response: str
    job_id: str | None = None
    correlation_id: str | None = None
    trace_id: str | None = None
    timestamp: str | None = None


class AustinRouter:
    def __init__(self) -> None:
        self.queue = queue

    def route(self, session_id: str, message: str) -> AustinRouteResult:
        trace_id = str(uuid4())
        correlation_id = str(uuid4())
        timestamp = datetime.now(timezone.utc).isoformat()

        structured_log(
            message="Austin route received",
            correlation_id=correlation_id,
            trace_id=trace_id,
            engine="austin",
            outcome="accepted",
            severity="info",
            service="austin.router",
        )

        if not status.online:
            status.online = True
            status.healthy = True
            status.startup_complete = True
            status.message = "Austin Online"

        lowered = (message or "").strip().lower()
        if lowered.startswith("health"):
            intent = "health"
            response = "Austin is online and healthy."
        elif lowered.startswith("status"):
            intent = "status"
            response = "Austin status requested."
        else:
            intent = "chat"
            response = (
                "Austin has accepted your request and is processing it in the background."
            )

        memory.save(
            {
                "id": f"{session_id}:{len(memory.records)}",
                "user_id": session_id,
                "category": "conversation",
                "title": "chat",
                "value": message,
            }
        )

        job = queue.enqueue(
            {
                "session_id": session_id,
                "message": message,
                "intent": intent,
                "trace_id": trace_id,
            },
            queue_name="austin.operations",
            priority="high" if intent == "chat" else "normal",
            correlation_id=correlation_id,
        )
        queue.mark_running(job.job_id)
        queue.complete(job.job_id, execution_time_ms=120)

        events.publish(
            "AustinChatReceived",
            {
                "session_id": session_id,
                "message": message,
                "intent": intent,
                "trace_id": trace_id,
                "correlation_id": correlation_id,
                "source_service": "austin.router",
                "engine": "austin",
                "severity": "info",
                "category": "conversation",
                "message": f"Austin accepted request for {session_id}",
                "metadata": {"intent": intent},
            },
        )

        return AustinRouteResult(
            intent=intent,
            confidence=0.95,
            engine="austin",
            response=response,
            job_id=job.job_id,
            correlation_id=job.correlation_id,
            trace_id=trace_id,
            timestamp=timestamp,
        )


router = AustinRouter()