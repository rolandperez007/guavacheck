"""
Engineering API

Endpoints for Engineering Engine.
"""

from fastapi import APIRouter

router = APIRouter(

    prefix="/engineering",

    tags=["Engineering"],

)


@router.get("")
async def index():

    return {

        "engine": "Engineering",

        "status": "ready",

    }


@router.get("/health")
async def health():

    return {

        "healthy": True

    }