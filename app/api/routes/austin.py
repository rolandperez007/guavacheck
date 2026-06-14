from typing import Any, Dict, Optional

from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(tags=["Austin"])


class AustinRequest(BaseModel):
    user_id: str
    action: str = "run_job"
    payload: Dict[str, Any]
    meta: Optional[Dict[str, Any]] = None


@router.post("/execute")
async def execute(payload: AustinRequest, request: Request):
    security = getattr(request.state, "irongate_result", None)

    query = payload.payload.get("query")

    return {
        "status": "success",
        "query": query,
        "user_id": payload.user_id,
        "action": payload.action,
        "meta": payload.meta,
        "security": security,
    }
