from __future__ import annotations

import time
import uuid
from typing import Dict, Any, Optional

# -----------------------------------
# In-memory job store (swap to Redis later)
# -----------------------------------
JOB_DB: Dict[str, Dict[str, Any]] = {}


class JobEngine:
    """
    Executes long-running tasks asynchronously.
    Works with IronGateway.
    """

    def create_job(self, job_type: str, payload: dict, user_id: str) -> str:
        job_id = str(uuid.uuid4())

        JOB_DB[job_id] = {
            "job_id": job_id,
            "type": job_type,
            "payload": payload,
            "user_id": user_id,
            "status": "queued",
            "created_at": time.time(),
            "result": None,
            "error": None,
        }

        return job_id

    # -----------------------------------
    # MAIN WORKER ENTRY (simulate worker)
    # -----------------------------------
    def process_job(self, job_id: str) -> Optional[Dict[str, Any]]:
        job = JOB_DB.get(job_id)

        if not job:
            return None

        try:
            job["status"] = "processing"

            # ROUTE BY TYPE
            if job["type"] == "pdf_export":
                result = self._generate_pdf(job["payload"])

            elif job["type"] == "boq_calculation":
                result = self._calculate_boq(job["payload"])

            elif job["type"] == "escrow":
                result = self._run_escrow(job["payload"])

            else:
                result = {"message": "Unknown job type"}

            job["status"] = "completed"
            job["result"] = result

        except Exception as e:
            job["status"] = "failed"
            job["error"] = str(e)

        return job

    # -----------------------------
    # TASKS (expand later)
    # -----------------------------
    def _generate_pdf(self, payload: dict) -> dict:
        time.sleep(2)  # simulate heavy work
        return {"file_url": "https://storage.fake/pdf/report.pdf", "size": "2.1MB"}

    def _calculate_boq(self, payload: dict) -> dict:
        return {"estimate": 2500000, "currency": "NGN"}

    def _run_escrow(self, payload: dict) -> dict:
        return {"escrow_status": "initiated"}
