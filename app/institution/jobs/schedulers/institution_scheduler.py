from __future__ import annotations

from collections.abc import Callable


class InstitutionScheduler:
    """
    Registers and executes recurring
    Institution Platform jobs.

    This class can later be backed by:

    • APScheduler
    • Celery Beat
    • Cron
    • Kubernetes CronJobs
    """

    def __init__(self) -> None:
        self._jobs: dict[str, Callable[[], None]] = {}

    def register(
        self,
        name: str,
        job: Callable[[], None],
    ) -> None:
        """
        Register a scheduled job.
        """
        self._jobs[name] = job

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove a registered job.
        """
        self._jobs.pop(name, None)

    def run(
        self,
        name: str,
    ) -> None:
        """
        Execute a registered job.
        """
        job = self._jobs.get(name)

        if job is None:
            raise ValueError(
                f"Unknown scheduled job '{name}'."
            )

        job()

    def run_all(self) -> None:
        """
        Execute every registered job.
        """
        for job in self._jobs.values():
            job()

    @property
    def jobs(self) -> list[str]:
        return sorted(self._jobs.keys())