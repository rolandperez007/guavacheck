"""
Austin Event Bus

Lightweight in-memory publish/subscribe event bus.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from typing import Any

Subscriber = Callable[[dict[str, Any]], None]


class EventBus:
    def __init__(self) -> None:
        self._subscribers = defaultdict(list)

    def subscribe(self, event_name: str, callback: Subscriber) -> None:
        self._subscribers[event_name].append(callback)

    def publish(self, event_name: str, payload: dict[str, Any]) -> None:
        for callback in self._subscribers[event_name]:
            callback(payload)


events = EventBus()
