# app/core/jobs/job_model.py

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class Job:
    job_id: str
    job_type: str
    payload: dict[str, Any]

    status: str = "queued"
    progress: int = 0

    result: dict[str, Any] | None = None
    error: str | None = None

    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
