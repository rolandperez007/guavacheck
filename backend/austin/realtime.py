from __future__ import annotations

from typing import Any

from .events import events
from .logger import logger
from api.websocket import manager


async def broadcast_event(event_name: str, payload: dict[str, Any] | None = None) -> None:
    payload = payload or {}
    await manager.broadcast(
        {
            "type": "austin-event",
            "event": event_name,
            "source": "Austin",
            "message": payload.get("message") or event_name,
            "payload": payload,
        }
    )


async def subscribe_to_events() -> None:
    def _handle(event) -> None:
        import asyncio

        try:
            loop = asyncio.get_running_loop()
            loop.create_task(broadcast_event(event.name, event.payload))
        except RuntimeError:
            logger.info("No running loop available for event broadcast")

    events.subscribe("AustinChatReceived", _handle)
