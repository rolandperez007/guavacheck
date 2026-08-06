"""
Austin API Routes
"""

from dataclasses import asdict

from fastapi import APIRouter
from pydantic import BaseModel

from backend.austin.event_store import store
from backend.austin.memory import memory
from backend.austin.queue import queue
from backend.austin.router import router as austin_router

router = APIRouter(
    prefix="/austin",
    tags=["Austin"],
)


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.get("/status")
async def status():

    return {
        "platform": "guavacheck",
        "status": "healthy",
        "austin": True,
        "message": "Austin Online",
    }


@router.post("/chat")
async def chat(request: ChatRequest):

    result = austin_router.route(
        session_id=request.session_id,
        message=request.message,
    )

    return asdict(result)


@router.get("/queue")
async def queue_summary():

    return queue.summary()


@router.get("/events")
async def list_events():
    return {
        "events": [
            {
                **asdict(event),
                "timestamp": event.timestamp.isoformat(),
            }
            for event in store.list()
        ]
    }


@router.get("/memory/{session_id}")
async def session_memory(session_id: str):

    return {
        "session_id": session_id,
        "history": memory.recall(session_id),
    }


@router.get("/jobs/{job_id}")
async def job(job_id: str):

    job = queue.get_job(job_id)

    if job is None:
        return {"error": "Job not found"}

    return asdict(job)
