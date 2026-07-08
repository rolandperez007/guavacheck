"""
Health API

Platform health endpoints.
"""

from fastapi import APIRouter

from austin.status import status

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("")
async def platform_health():

    return {

        "platform": "guavacheck",

        "status": "healthy" if status.healthy else "degraded",

        "austin": status.online,

        "registered_engines": status.registered_engines,

        "message": status.message,

    }


@router.get("/live")
async def live():

    return {

        "alive": True

    }


@router.get("/ready")
async def ready():

    return {

        "ready": status.startup_complete

    }