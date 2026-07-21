"""
guavacheck Backend API

Main FastAPI application entry point.
"""

from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.austin.bootstrap import initialize, startup_async
from backend.austin.kernel import AustinContextMiddleware
from backend.core.router_registry import register_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application startup/shutdown lifecycle.
    """

    # Initialize Austin core
    initialize()

    # Start Austin realtime services
    await startup_async()

    yield

    # Future shutdown tasks go here
    # e.g. await shutdown_async()


def create_application() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """

    app = FastAPI(
        title="guavacheck API",
        description="AI-powered property verification, engineering and intelligence platform.",
        version="1.0.0",
        lifespan=lifespan,
    )

    # Austin request context
    app.add_middleware(AustinContextMiddleware)

    # Register API routes
    register_routers(app)

    return app


app = create_application()