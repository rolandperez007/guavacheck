"""
Austin Event Broadcaster

Broadcasts Austin events to all connected
Engineering Command Center dashboards.
"""

from __future__ import annotations

import asyncio
from dataclasses import asdict

from ..models import AustinEvent
from .manager import realtime_manager


def broadcast_event(event: AustinEvent) -> None:
    """
    Broadcast a newly created Austin event.
    """

    payload = asdict(event)
    payload["timestamp"] = event.timestamp.isoformat()

    try:
        loop = asyncio.get_running_loop()

        loop.create_task(realtime_manager.broadcast(payload))

    except RuntimeError:
        # Server isn't running an event loop yet.
        pass
