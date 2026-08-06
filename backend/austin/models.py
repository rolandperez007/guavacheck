from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
from uuid import uuid4


@dataclass
class AustinEvent:
    event_id: str
    timestamp: datetime
    correlation_id: str
    event_type: str
    source_service: str
    engine: str
    severity: str
    category: str
    message: str
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def create(
        cls,
        *,
        event_type: str,
        source_service: str,
        engine: str,
        severity: str,
        category: str,
        message: str,
        correlation_id: str | None = None,
        metadata: dict[str, Any] | None = None,
        timestamp: datetime | None = None,
    ) -> AustinEvent:
        return cls(
            event_id=str(uuid4()),
            timestamp=timestamp or datetime.now(timezone.utc),
            correlation_id=correlation_id or str(uuid4()),
            event_type=event_type,
            source_service=source_service,
            engine=engine,
            severity=severity,
            category=category,
            message=message,
            metadata=metadata or {},
        )
