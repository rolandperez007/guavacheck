from fastapi import APIRouter

router = APIRouter(
    prefix="/exports",
    tags=["Exports"],
)


@router.get("/health")
def health():

    return {
        "module": "exports",
        "status": "online",
    }
