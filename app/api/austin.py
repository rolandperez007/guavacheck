from fastapi import APIRouter
from pydantic import BaseModel

from app.agents.swarm.swarm_coordinator import SwarmCoordinator

router = APIRouter()

coordinator = SwarmCoordinator()


class AustinRequest(BaseModel):
    user_id: str
    message: str


@router.post("/execute")
async def chat(request: AustinRequest):

    result = await coordinator.run(
        user_id=request.user_id,
        query=request.message
    )

    return result