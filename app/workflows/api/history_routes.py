from fastapi import APIRouter

router = APIRouter(
    prefix="/history",
)


@router.get("/{execution_id}")
async def history(
    execution_id: str,
):

    return {
        "execution": execution_id,
        "history": [],
    }