from fastapi import APIRouter
from pydantic import BaseModel
from app.core.austin_engine import AustinEngine

router = APIRouter()
engine = AustinEngine()


class AustinRequest(BaseModel):
    query: str
    user_id: str | None = None


@router.post("/execute")
async def execute(req: AustinRequest):

    result = await engine.execute(
        query=req.query,
        user_id=req.user_id
    )

    return result


@router.get("/")
def health():
    return {"status": "Austin running v2"}