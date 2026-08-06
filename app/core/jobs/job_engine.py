# app/core/jobs/job_engine.py

import uuid
from datetime import datetime

from app.core.jobs.job_queue import job_queue
from app.core.jobs.job_store import JobStore


class JobEngine:
    def __init__(self, store: JobStore):
        self.store = store

    async def submit(self, job_type: str, payload: dict, idempotency_key: str = None):
        job_id = str(uuid.uuid4())

        job = {
            "job_id": job_id,
            "job_type": job_type,
            "payload": payload,
            "status": "queued",
            "progress": 0,
            "created_at": datetime.utcnow().isoformat(),
        }

        # 1. Persist job
        self.store.create_job(job)

        # 2. Push to Redis queue
        job_queue.enqueue("app.core.jobs.worker.process_job", job_id, job_type, payload)

        return {"job_id": job_id, "status": "queued"}
