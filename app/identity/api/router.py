from fastapi import APIRouter


router = APIRouter(
    prefix="/identity",
    tags=["Identity"]
)


@router.get("/")
def identity_status():

    return {
        "module": "identity",
        "status": "active"
    }