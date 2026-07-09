"""
guavacheck API Router Registry

Central registration point for all backend routes.
"""

from fastapi import FastAPI


def register_routers(app: FastAPI):
    """
    Register every API router.
    """

    # -----------------------------
    # Platform Health
    # -----------------------------
    from api.routes.health import (
        router as health_router,
    )

    app.include_router(
        health_router
    )

    # -----------------------------
    # Austin
    # -----------------------------
    from api.routes.austin import (
        router as austin_router,
    )

    app.include_router(
        austin_router
    )

    # -----------------------------
    # WebSocket
    # -----------------------------
    from api.websocket import (
        router as websocket_router,
    )

    app.include_router(
        websocket_router
    )

    # -----------------------------
    # Engineering
    # -----------------------------
    from api.routes.engineering import (
        router as engineering_router,
    )

    app.include_router(
        engineering_router
    )

    # -----------------------------
    # Verification Engine
    # -----------------------------
    from verification_engine.api.verification_routes import (
        router as verification_router,
    )

    app.include_router(
        verification_router
    )

    return app