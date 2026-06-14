from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from app.core.security.security import get_current_user
from app.core.security.context_builder import build_context

from app.agents.swarm.swarm_coordinator import SwarmCoordinator

router = APIRouter()

coordinator = SwarmCoordinator()


class AustinRequest(BaseModel):
    user_id: str
    message: str


@router.post("/execute")
async def chat(request: AustinRequest, user=Depends(get_current_user)):
    context = build_context(user)

    result = await coordinator.run(
        user_id=context.user_id, query=request.message, context=context
    )

    return result
