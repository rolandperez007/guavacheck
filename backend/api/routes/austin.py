"""
Austin API Routes
"""
from dataclasses import asdict
from fastapi import APIRouter
from pydantic import BaseModel
from austin.queue import queue
from austin.router import router as austin_router
from austin.event_store import store

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
        request.session_id,
        request.message,
    )

    return result.__dict__

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