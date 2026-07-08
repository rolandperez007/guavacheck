"""
Austin API

Public endpoints for Austin.
"""

from fastapi import APIRouter

from austin.router import router as austin_router
from austin.status import status

router = APIRouter(

    prefix="/austin",

    tags=["Austin"],

)


@router.get("/status")
async def austin_status():

    return {

        "online": status.online,

        "healthy": status.healthy,

        "message": status.message,

        "engines": status.registered_engines,

    }


@router.post("/chat")
async def chat(payload: dict):

    session_id = payload.get(

        "session_id",

        "anonymous",

    )

    message = payload.get(

        "message",

        "",

    )

    result = austin_router.route(

        session_id,

        message,

    )

    return {

        "intent": result.intent,

        "confidence": result.confidence,

        "engine": result.engine,

        "response": result.response,

    }