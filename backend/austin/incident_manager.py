from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class Incident:
    severity: str
    affected_services: list[str]
    affected_customers: int
    estimated_revenue_impact: float
    likely_root_cause: str
    recovery_status: str
    recommendation: str
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class IncidentManager:
    def __init__(self) -> None:
        self._incidents: list[Incident] = []

    def create_incident(self, **kwargs: Any) -> Incident:
        incident = Incident(**kwargs)
        self._incidents.append(incident)
        return incident

    def list(self) -> list[Incident]:
        return list(self._incidents)


manager = IncidentManager()
