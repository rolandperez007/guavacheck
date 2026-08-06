from fastapi import APIRouter

router = APIRouter(
    prefix="/events",
)


@router.get("/")
async def list_events():

    return {
        "events": [],
    }


@router.post("/publish")
async def publish():

    return {
        "published": True,
    }