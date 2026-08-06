from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
)


@router.get("/dashboard")
async def dashboard():

    return {
        "dashboard": {},
    }


@router.get("/metrics")
async def metrics():

    return {
        "metrics": {},
    }


@router.get("/insights")
async def insights():

    return {
        "insights": [],
    }