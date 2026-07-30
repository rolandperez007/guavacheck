from fastapi import APIRouter

router = APIRouter(
    prefix="/rooms",
    tags=["Vision Rooms"],
)


@router.get("/health")
def health():

    return {
        "module": "rooms",
        "status": "online",
    }