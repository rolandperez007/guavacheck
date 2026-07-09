"""
guavacheck Backend API

Main FastAPI application entry point.
"""

from fastapi import FastAPI

from core.router_registry import register_routers
from austin.bootstrap import initialize
from austin.kernel import AustinContextMiddleware


def create_application():

    app = FastAPI(

        title="guavacheck API",

        description=(
            "AI-powered property verification, "
            "engineering and intelligence platform."
        ),

        version="1.0.0"

    )

    app.add_middleware(AustinContextMiddleware)

    register_routers(app)

    # Start Austin
    initialize()

    return app


app = create_application()