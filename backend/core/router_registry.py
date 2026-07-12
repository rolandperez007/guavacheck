"""
guavacheck API Router Registry

Central registration point for all backend routes.
"""

from fastapi import FastAPI
from api.routes.austin_ws import router as austin_ws_router

from fastapi import FastAPI


def register_routers(app: FastAPI) -> None:
    """
    Register all API routers.
    """

    from api.routes.austin import router as austin_router
    from api.routes.austin_ws import router as austin_ws_router
    from api.routes.health import router as health_router

    # Health endpoints
    app.include_router(health_router)

    # Austin API
    app.include_router(austin_router)

    # Austin WebSocket API
    app.include_router(austin_ws_router)