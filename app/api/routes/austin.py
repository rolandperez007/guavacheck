from fastapi import APIRouter
from pydantic import BaseModel

from app.core.austin_orchestrator import AustinOrchestrator

router = APIRouter()

orchestrator = AustinOrchestrator()

class AustinRequest(BaseModel):
    user_id: str
    query: str

@router.post('/execute')
def execute(req: AustinRequest):
    return orchestrator.run(
        user_id=req.user_id,
        query=req.query
    )
