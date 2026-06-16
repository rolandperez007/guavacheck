from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.austin_orchestrator import AustinOrchestrator
from app.main import verify_api_key

router = APIRouter(dependencies=[Depends(verify_api_key)])

orchestrator = AustinOrchestrator()


class AustinRequest(BaseModel):
    user_id: str
    query: str


@router.post("/execute")
def execute(req: AustinRequest):

    result = orchestrator.run(
        user_id=req.user_id,
        query=req.query
    )

    return result

    