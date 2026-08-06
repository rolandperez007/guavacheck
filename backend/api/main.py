"""
GuavaCheck API

Main FastAPI application entrypoint.
"""

from __future__ import annotations

import threading
from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.api.routes.austin import router as austin_router
from backend.austin.bootstrap import bootstrap_austin
from backend.austin.worker import worker

# ---------------------------------------------------------------------
# Austin Worker
# ---------------------------------------------------------------------

_worker_thread: threading.Thread | None = None


def start_austin_worker() -> None:
    """
    Start Austin's background worker exactly once.
    """

    global _worker_thread

    if _worker_thread and _worker_thread.is_alive():
        return

    _worker_thread = threading.Thread(
        target=worker.run,
        daemon=True,
        name="AustinWorker",
    )

    _worker_thread.start()


# ---------------------------------------------------------------------
# Application Lifecycle
# ---------------------------------------------------------------------


@asynccontextmanager
async def lifespan(app: FastAPI):

    bootstrap_austin()

    start_austin_worker()

    print("=" * 70)
    print("GuavaCheck API Online")
    print("Austin Worker Online")
    print("=" * 70)

    yield

    print("=" * 70)
    print("GuavaCheck API Shutdown")
    print("=" * 70)


# ---------------------------------------------------------------------
# FastAPI
# ---------------------------------------------------------------------

app = FastAPI(
    title="GuavaCheck API",
    version="1.0.0",
    description="GuavaCheck Platform API",
    lifespan=lifespan,
)

# ---------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------

app.include_router(austin_router)


@app.get("/")
async def root():
    return {
        "platform": "guavacheck",
        "status": "online",
        "austin": "online",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "worker": (_worker_thread.is_alive() if _worker_thread else False),
    }
