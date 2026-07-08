"""
Austin Router

Provides the minimal routing surface Austin exposes to the API.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .logger import logger
from .memory import memory
from .status import status


@dataclass
class AustinRouteResult:
    intent: str
    confidence: float
    engine: str
    response: str


class AustinRouter:
    def route(self, session_id: str, message: str) -> AustinRouteResult:
        logger.info("Austin route | session=%s message=%s", session_id, message)

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
            response = f"Austin received: {message}"

        memory.save(
            {
                "id": f"{session_id}:{len(memory.records)}",
                "user_id": session_id,
                "category": "conversation",
                "title": "chat",
                "value": message,
            }
        )

        return AustinRouteResult(
            intent=intent,
            confidence=0.95,
            engine="austin",
            response=response,
        )


router = AustinRouter()