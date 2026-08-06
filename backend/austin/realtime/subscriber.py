"""
Austin Realtime Event Subscriber

Registers realtime listeners on the Austin Event Bus.
"""

from __future__ import annotations

from ..events import events
from .broadcaster import broadcast_event


async def subscribe_to_events() -> None:
    """
    Subscribe realtime broadcasting to Austin events.
    """

    events.subscribe(
        "AustinChatReceived",
        broadcast_event,
    )
