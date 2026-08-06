import time

from fastapi import APIRouter

router = APIRouter()

START_TIME = time.time()


@router.get("/health")
def health():
    return {
        "status": "ok",
        "service": "austin-v3",
        "uptime_seconds": int(time.time() - START_TIME),
    }


@router.get("/ready")
def ready():
    return {"ready": True, "database": "assumed-ok", "cache": "assumed-ok"}


@router.get("/status")
def status():
    return {
        "system": "healthy",
        "modules": {"engine": "online", "agents": "online", "memory": "online"},
    }
