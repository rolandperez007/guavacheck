from __future__ import annotations

from typing import Any, Protocol


class EventPublisher(Protocol):
    def publish(
        self, event_type: str, payload: dict[str, Any] | None = None
    ) -> None: ...


class MetricsCollector(Protocol):
    def collect(self, *, engine: str, metrics: dict[str, Any]) -> None: ...


class RecommendationEngine(Protocol):
    def explain(
        self, *, queue_depth: int, active_workers: int, wait_time_ms: int | None = None
    ) -> dict[str, Any]: ...


class TrustTracker(Protocol):
    def snapshot(self) -> dict[str, Any]: ...
