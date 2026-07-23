"""
Austin Runtime Health

Reports the operational health of the Austin runtime.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from backend.austin.queue import queue


@dataclass(slots=True)
class RuntimeHealth:

    status: str
    timestamp: str
    worker_running: bool
    queued_jobs: int
    running_jobs: int
    completed_jobs: int
    failed_jobs: int


class RuntimeHealthService:

    def get_health(
        self,
        *,
        worker_running: bool,
    ) -> RuntimeHealth:

        summary = queue.summary()

        status = "healthy"

        if not worker_running:
            status = "degraded"

        if summary["failed"] > 0:
            status = "warning"

        return RuntimeHealth(
            status=status,
            timestamp=datetime.now(
                timezone.utc
            ).isoformat(),
            worker_running=worker_running,
            queued_jobs=summary["queued"],
            running_jobs=summary["running"],
            completed_jobs=summary["completed"],
            failed_jobs=summary["failed"],
        )


runtime_health = RuntimeHealthService()