from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel, Field

from irongate.bootstrap import gate
from irongate.normalizer import normalize_request
from irongate import audit

router = APIRouter(prefix="/irongate", tags=["IronGate"])


class IronGateEvaluateRequest(BaseModel):
    user_id: Optional[str] = Field(None, description="Logical user identifier")
    action: Optional[str] = Field(None, description="Requested action")
    payload: Optional[Dict[str, Any]] = Field(default_factory=dict)
    meta: Optional[Dict[str, Any]] = None


class IronGateEvaluateResponse(BaseModel):
    allowed: bool
    score: int
    decision: str
    decision_id: str
    reason: Optional[str] = None
    reasons: Optional[List[str]] = None
    rules_triggered: Optional[List[Dict[str, Any]]] = None
    final_action: Optional[str] = None


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
