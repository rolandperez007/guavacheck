from fastapi import APIRouter

router = APIRouter(
    prefix="/furniture",
    tags=["Furniture"],
)


@router.get("/health")
def health():

    return {
        "module": "furniture",
        "status": "online",
    }