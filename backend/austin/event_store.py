from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Any

from .models import AustinEvent


class AustinEventStore:
    def __init__(self) -> None:
        self._events: list[AustinEvent] = []

    def append(self, event: AustinEvent) -> AustinEvent:
        self._events.append(event)

        print("=" * 70)
        print(f"EVENT STORED -> {len(self._events)}")
        print(event)
        print("=" * 70)

        return event

    def list(self, *, window: str = "1h", engine: str | None = None, severity: str | None = None, category: str | None = None, correlation_id: str | None = None) -> list[AustinEvent]:
        now = datetime.now(timezone.utc)
        if window == "1h":
            cutoff = now - timedelta(hours=1)
        elif window == "24h":
            cutoff = now - timedelta(hours=24)
        elif window == "7d":
            cutoff = now - timedelta(days=7)
        else:
            cutoff = now - timedelta(hours=1)

        filtered = [event for event in self._events if event.timestamp >= cutoff]
        if engine:
            filtered = [event for event in filtered if event.engine == engine]
        if severity:
            filtered = [event for event in filtered if event.severity == severity]
        if category:
            filtered = [event for event in filtered if event.category == category]
        if correlation_id:
            filtered = [event for event in filtered if event.correlation_id == correlation_id]
        return sorted(filtered, key=lambda item: item.timestamp, reverse=True)

    def summary(self) -> dict[str, Any]:
        return {
            "total": len(self._events),
            "last_hour": len(self.list(window="1h")),
            "last_24h": len(self.list(window="24h")),
            "last_7d": len(self.list(window="7d")),
        }


store = AustinEventStore()
