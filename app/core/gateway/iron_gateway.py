from __future__ import annotations

import hashlib
import json
import time
from dataclasses import dataclass
from typing import Any, Dict, Optional

# -----------------------------
# Simple in-memory job store
# (swap later with Redis / DB)
# -----------------------------
JOB_STORE: Dict[str, Dict[str, Any]] = {}


def _generate_idempotency_key(user_id: str, payload: dict) -> str:
    """
    Creates a deterministic key so duplicate requests
    do not generate duplicate jobs.
    """
    raw = f"{user_id}:{json.dumps(payload, sort_keys=True)}"
    return hashlib.sha256(raw.encode()).hexdigest()


def _generate_job_id() -> str:
    return hashlib.sha256(str(time.time()).encode()).hexdigest()


# -----------------------------
# Routing result structure
# -----------------------------
@dataclass
class GatewayResponse:
    job_id: str
    status: str
    message: str
    cached: bool = False


# -----------------------------
# IRON GATEWAY CORE
# -----------------------------
class IronGateway:
    """
    Single entry point for all heavy system requests.
    """

    def __init__(self, job_store: Dict[str, Dict[str, Any]] = None):
        self.job_store = job_store if job_store is not None else JOB_STORE

    # -------------------------
    # MAIN ENTRY METHOD
    # -------------------------
    def handle_request(
        self, user_id: str, payload: Dict[str, Any], request_type: str = "generic"
    ) -> GatewayResponse:
        # 1. Create idempotency key
        idem_key = _generate_idempotency_key(user_id, payload)

        # 2. Check for duplicate request
        existing_job = self._find_by_idempotency_key(idem_key)
        if existing_job:
            return GatewayResponse(
                job_id=existing_job["job_id"],
                status=existing_job["status"],
                message="Existing job returned (idempotent hit)",
                cached=True,
            )

        # 3. Create new job
        job_id = _generate_job_id()

        job_record = {
            "job_id": job_id,
            "user_id": user_id,
            "payload": payload,
            "type": request_type,
            "status": "queued",
            "created_at": time.time(),
            "idempotency_key": idem_key,
            "result": None,
            "error": None,
        }

        self.job_store[job_id] = job_record

        # 4. Dispatch job to async layer (placeholder hook)
        self._dispatch(job_record)

        return GatewayResponse(
            job_id=job_id,
            status="queued",
            message="Job created and dispatched",
            cached=False,
        )

    # -------------------------
    # INTERNAL: duplicate check
    # -------------------------
    def _find_by_idempotency_key(self, key: str) -> Optional[Dict[str, Any]]:
        for job in self.job_store.values():
            if job.get("idempotency_key") == key:
                return job
        return None

    # -------------------------
    # INTERNAL: dispatcher hook
    # -------------------------
    def _dispatch(self, job: Dict[str, Any]) -> None:
        """
        This is where we plug:
        - Ingest worker (Trigger.dev / Celery / BullMQ equivalent)
        - execution engine
        - PDF generator
        - escrow engine
        """

        # IMPORTANT:
        # We intentionally DO NOT process here.

        job["status"] = "dispatched"

        # Future hook example:
        # event_bus.publish("job.created", job)
