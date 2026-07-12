"""
Austin Realtime Event Subscriber

Registers realtime listeners on the Austin Event Bus.
"""

from __future__ import annotations

from .broadcaster import broadcast_event
from ..events import events


async def subscribe_to_events() -> None:
    """
    Subscribe realtime broadcasting to Austin events.
    """

    events.subscribe(
        "AustinChatReceived",
        broadcast_event,
    )