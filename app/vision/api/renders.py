from fastapi import APIRouter

router = APIRouter(
    prefix="/renders",
    tags=["Vision Renders"],
)


@router.get("/health")
def health():

    return {
        "module": "renders",
        "status": "online",
    }
