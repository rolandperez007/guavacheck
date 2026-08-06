from fastapi import APIRouter

router = APIRouter(
    prefix="/revisions",
    tags=["Revisions"],
)


@router.get("/health")
def health():

    return {
        "module": "revisions",
        "status": "online",
    }
