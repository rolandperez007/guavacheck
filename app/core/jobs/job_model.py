# app/core/jobs/job_model.py

from dataclasses import dataclass
from typing import Any, Dict, Optional
from datetime import datetime


@dataclass
class Job:
    job_id: str
    job_type: str
    payload: Dict[str, Any]

    status: str = "queued"
    progress: int = 0

    result: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
