"""
Austin Runtime Scheduler

Responsible for selecting the next executable job from the queue.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone

from backend.austin.queue import queue


@dataclass(slots=True)
class SchedulerDecision:
    """
    Represents a scheduling decision.
    """

    job: object | None
    reason: str
    timestamp: str


class RuntimeScheduler:
    """
    Selects the next Austin job for execution.
    """

    def next_job(self) -> SchedulerDecision:

        job = queue.next()

        if job is None:

            return SchedulerDecision(
                job=None,
                reason="No queued jobs.",
                timestamp=datetime.now(
                    timezone.utc
                ).isoformat(),
            )

        return SchedulerDecision(
            job=job,
            reason="Queued job available.",
            timestamp=datetime.now(
                timezone.utc
            ).isoformat(),
        )

    def queue_depth(self) -> int:

        return queue.summary()["queued"]

    def has_work(self) -> bool:

        return self.queue_depth() > 0


scheduler = RuntimeScheduler()
