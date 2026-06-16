from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# ---- Request model ----
class ControlRequest(BaseModel):
    query: str
    user_id: str | None = "anonymous"


# ---- Basic test endpoint ----
@router.get("/health")
def health():
    return {"status": "irongate online"}


# ---- Simple command endpoint (for Austin later) ----
@router.post("/command")
def command(req: ControlRequest):
    return {
        "message": "command received",
        "query": req.query,
        "user": req.user_id
    }