"""
Austin Event Repository

Wraps the Austin Event Store.

This layer exists so that future database
storage requires no changes to routers.
"""

from __future__ import annotations

from austin.event_store import store
from austin.models import AustinEvent


class EventRepository:

    def all(self) -> list[AustinEvent]:

        return store.list()

    def save(
        self,
        event: AustinEvent,
    ) -> None:

        store.append(event)

    def clear(self) -> None:

        store.clear()


event_repository = EventRepository()