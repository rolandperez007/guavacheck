"""
Austin Background Queue

Provides a lightweight in-memory queue for Austin jobs so requests can be
acknowledged immediately and tracked through a production-style lifecycle.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass
class AustinJob:
    job_id: str
    correlation_id: str
    queue_name: str
    priority: str
    retry_policy: dict[str, Any]
    timeout_seconds: int
    status: str = "queued"
    execution_time_ms: int | None = None
    failure_reason: str | None = None
    created_at: datetime = field(default_factory=datetime.utcnow)
    started_at: datetime | None = None
    completed_at: datetime | None = None
    attempts: int = 0
    payload: dict[str, Any] = field(default_factory=dict)


class AustinJobQueue:
    def __init__(self) -> None:
        self._jobs: dict[str, AustinJob] = {}

    def enqueue(
        self,
        payload: dict[str, Any],
        *,
        queue_name: str = "austin.default",
        priority: str = "normal",
        timeout_seconds: int = 30,
        max_retries: int = 3,
        correlation_id: str | None = None,
    ) -> AustinJob:
        job_id = str(uuid4())
        correlation_id = correlation_id or str(uuid4())
        job = AustinJob(
            job_id=job_id,
            correlation_id=correlation_id,
            queue_name=queue_name,
            priority=priority,
            retry_policy={
                "max_retries": max_retries,
                "backoff_seconds": 5,
            },
            timeout_seconds=timeout_seconds,
            payload=payload,
        )
        self._jobs[job_id] = job
        return job

    def get_job(self, job_id: str) -> AustinJob | None:
        return self._jobs.get(job_id)
    
    def next(self) -> AustinJob | None:
        """
        Return the next queued job.
        """

        for job in self._jobs.values():
            if job.status == "queued":
                return job

            return None

    def all_jobs(self) -> list[AustinJob]:
        """
        Return every job.
        """

        return list(self._jobs.values())

    def mark_running(self, job_id: str) -> AustinJob | None:
        job = self._jobs.get(job_id)
        if not job:
            return None
        job.status = "running"
        job.started_at = datetime.utcnow()
        job.attempts += 1
        return job

    def complete(self, job_id: str, execution_time_ms: int | None = None) -> AustinJob | None:
        job = self._jobs.get(job_id)
        if not job:
            return None
        job.status = "completed"
        job.execution_time_ms = execution_time_ms
        job.completed_at = datetime.utcnow()
        return job

    def fail(self, job_id: str, reason: str) -> AustinJob | None:
        job = self._jobs.get(job_id)
        if not job:
            return None
        job.status = "failed"
        job.failure_reason = reason
        job.completed_at = datetime.utcnow()
        return job

    def summary(self) -> dict[str, Any]:
        jobs = list(self._jobs.values())
        return {
            "queued": sum(1 for job in jobs if job.status == "queued"),
            "running": sum(1 for job in jobs if job.status == "running"),
            "completed": sum(1 for job in jobs if job.status == "completed"),
            "failed": sum(1 for job in jobs if job.status == "failed"),
            "total": len(jobs),
        }


queue = AustinJobQueue()
