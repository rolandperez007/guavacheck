"""
Austin Runtime Readiness

Determines whether Austin is ready
to accept new work.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.austin.queue import queue


@dataclass(slots=True)
class RuntimeReadiness:
    ready: bool

    reason: str

    queue_depth: int


class RuntimeReadinessService:
    MAX_QUEUE_DEPTH = 500

    def check(self) -> RuntimeReadiness:

        summary = queue.summary()

        if summary["queued"] > self.MAX_QUEUE_DEPTH:
            return RuntimeReadiness(
                ready=False,
                reason="Queue overload",
                queue_depth=summary["queued"],
            )

        return RuntimeReadiness(
            ready=True,
            reason="Runtime ready",
            queue_depth=summary["queued"],
        )


runtime_readiness = RuntimeReadinessService()
