# app/api/routes/austin.py

from fastapi import APIRouter

from app.core.austin_engine import AustinEngine
from app.models.request_models import AustinExecuteRequest

router = APIRouter()

engine = AustinEngine()

@router.post("/austin/execute")
async def execute(req: AustinExecuteRequest):

    return await engine.execute(
        req.input,
        req.context
    )