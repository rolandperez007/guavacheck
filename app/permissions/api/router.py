from fastapi import APIRouter


router = APIRouter(
    prefix="/permissions",
    tags=["Permissions"]
)


@router.get("/")

def permissions_status():

    return {
        "module": "permissions",
        "status": "active"
    }