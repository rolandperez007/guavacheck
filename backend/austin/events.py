"""
Austin Event Bus

The Event Bus allows every subsystem inside guavacheck
to communicate without depending directly on one another.

Austin listens.
Austin publishes.
Austin coordinates.
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

from .event_store import store
from .logger import logger
from .models import AustinEvent


@dataclass
class Event:
    name: str
    payload: dict[str, Any]
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class EventBus:
    def __init__(self) -> None:
        self.listeners: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(
        self,
        event_name: str,
        callback: Callable,
    ) -> None:
        self.listeners[event_name].append(callback)
        logger.info("Subscribed -> %s", event_name)

    def publish(
        self,
        event_name: str,
        payload: dict[str, Any] | None = None,
    ) -> None:

        print()
        print("=" * 70)
        print(f"PUBLISH CALLED -> {event_name}")
        print("=" * 70)

        payload = payload or {}

        correlation_id = payload.get("correlation_id") or str(
            payload.get("trace_id") or "anon"
        )

        event = AustinEvent.create(
            event_type=event_name,
            source_service=payload.get("source_service", "austin"),
            engine=payload.get("engine", "austin"),
            severity=payload.get("severity", "info"),
            category=payload.get("category", "operations"),
            message=payload.get("message", event_name),
            correlation_id=correlation_id,
            metadata=payload.get("metadata", {}),
        )

        print("ABOUT TO APPEND EVENT")
        store.append(event)
        print("APPEND COMPLETE")
        print(f"STORE SIZE = {len(store._events)}")

        logger.info(
            "Event -> %s | correlation_id=%s | severity=%s",
            event_name,
            event.correlation_id,
            event.severity,
        )

        for callback in self.listeners[event_name]:
            try:
                callback(event)
            except Exception as exc:
                logger.exception(
                    "Event '%s' failed: %s",
                    event_name,
                    exc,
                )

    def registered_events(self):
        return sorted(self.listeners.keys())

    def listener_count(self):
        return sum(len(v) for v in self.listeners.values())


events = EventBus()
