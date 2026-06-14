from fastapi import APIRouter
from irongate.telemetry import get_metrics, get_recent

router = APIRouter()


@router.get("/irongate/metrics")
def metrics():
    return get_metrics()


@router.get("/irongate/recent")
def recent():
    return get_recent()
