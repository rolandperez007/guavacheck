from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from ..business_monitor import monitor
from ..event_store import store
from ..events import events
from ..incident_manager import manager
from ..logger import logger, structured_log
from ..queue import queue
from ..recommendations import AustinRecommendations
from ..trust import TrustMonitor


@dataclass
class AustinKernel:
    event_bus: Any = field(default_factory=lambda: events)
    event_store: Any = field(default_factory=lambda: store)
    queue_service: Any = field(default_factory=lambda: queue)
    logger_service: Any = field(default_factory=lambda: logger)
    structured_logger: Any = field(default_factory=lambda: structured_log)
    incident_reporter: Any = field(default_factory=lambda: manager)
    business_monitor: Any = field(default_factory=lambda: monitor)
    recommendation_engine: Any = field(default_factory=lambda: AustinRecommendations())
    trust_tracker: Any = field(default_factory=lambda: TrustMonitor())

    def publish_event(self, event_type: str, payload: dict[str, Any] | None = None) -> None:
        base_payload = payload or {}
        self.event_bus.publish(event_type, base_payload)

    def log(self, *, message: str, correlation_id: str | None = None, trace_id: str | None = None, engine: str = "austin", duration_ms: int | None = None, outcome: str = "ok", severity: str = "info", service: str = "austin") -> None:
        self.structured_logger(
            message=message,
            correlation_id=correlation_id,
            trace_id=trace_id,
            engine=engine,
            duration_ms=duration_ms,
            outcome=outcome,
            severity=severity,
            service=service,
        )

    def recommend(self, *, queue_depth: int, active_workers: int, wait_time_ms: int | None = None) -> dict[str, Any]:
        return self.recommendation_engine.explain(queue_depth=queue_depth, active_workers=active_workers, wait_time_ms=wait_time_ms)

    def track_trust(self) -> dict[str, Any]:
        return self.trust_tracker.snapshot()
