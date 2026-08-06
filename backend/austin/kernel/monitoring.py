from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class MonitoringThresholds:
    queue_depth_warning: int = 100
    queue_depth_critical: int = 300
    wait_time_warning_ms: int = 1000
    wait_time_critical_ms: int = 3000
    worker_utilization_warning: int = 80
    worker_utilization_critical: int = 95


class MonitoringConfig:
    def __init__(self, thresholds: MonitoringThresholds | None = None) -> None:
        self.thresholds = thresholds or MonitoringThresholds()

    def evaluate(
        self,
        *,
        queue_depth: int,
        active_workers: int,
        wait_time_ms: int,
        worker_utilization: int,
    ) -> dict[str, Any]:
        return {
            "status": "warning"
            if queue_depth > self.thresholds.queue_depth_warning
            or wait_time_ms > self.thresholds.wait_time_warning_ms
            or worker_utilization > self.thresholds.worker_utilization_warning
            else "healthy",
            "queue_depth": queue_depth,
            "active_workers": active_workers,
            "wait_time_ms": wait_time_ms,
            "worker_utilization": worker_utilization,
            "thresholds": self.thresholds.__dict__,
        }
