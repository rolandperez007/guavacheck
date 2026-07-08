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
from dataclasses import dataclass
from datetime import datetime
from typing import Callable, Any

from .logger import logger


@dataclass
class Event:

    name: str

    payload: dict[str, Any]

    timestamp: datetime = datetime.utcnow()


class EventBus:

    def __init__(self):

        self.listeners = defaultdict(list)

    def subscribe(

        self,

        event_name: str,

        callback: Callable,

    ):

        self.listeners[event_name].append(callback)

        logger.info(

            "Subscribed -> %s",

            event_name,

        )

    def publish(

        self,

        event_name: str,

        payload: dict[str, Any] | None = None,

    ):

        payload = payload or {}

        logger.info(

            "Event -> %s",

            event_name,

        )

        event = Event(

            name=event_name,

            payload=payload,

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

        return sum(

            len(v)

            for v in self.listeners.values()

        )


events = EventBus()