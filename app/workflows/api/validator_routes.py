from fastapi import APIRouter

router = APIRouter(
    prefix="/validate",
)


@router.post("/")
async def validate():

    return {
        "valid": True,
        "errors": [],
    }