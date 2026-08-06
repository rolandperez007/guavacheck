from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from irongate import audit
from irongate.bootstrap import gate
from irongate.normalizer import normalize_request

router = APIRouter(prefix="/irongate", tags=["IronGate"])


class IronGateEvaluateRequest(BaseModel):
    user_id: str | None = Field(None, description="Logical user identifier")
    action: str | None = Field(None, description="Requested action")
    payload: dict[str, Any] | None = Field(default_factory=dict)
    meta: dict[str, Any] | None = None


class IronGateEvaluateResponse(BaseModel):
    allowed: bool
    score: int
    decision: str
    decision_id: str
    reason: str | None = None
    reasons: list[str] | None = None
    rules_triggered: list[dict[str, Any]] | None = None
    final_action: str | None = None


@router.post("/evaluate", response_model=IronGateEvaluateResponse)
async def evaluate_irongate(request: Request, data: IronGateEvaluateRequest):
    payload = data.model_dump() if hasattr(data, "model_dump") else data.dict()
    context = normalize_request(request, payload)
    result = gate.evaluate(context)

    try:
        audit.log_event(context, result)
    except Exception:
        pass

    return result


@router.post("/test")
async def test_irongate(data: IronGateEvaluateRequest):
    payload = data.model_dump() if hasattr(data, "model_dump") else data.dict()
    return {
        "ok": True,
        "received": payload,
    }
