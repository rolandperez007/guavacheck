from fastapi import APIRouter

router = APIRouter(
    prefix="/materials",
    tags=["Materials"],
)


@router.get("/health")
def health():

    return {
        "module": "materials",
        "status": "online",
    }