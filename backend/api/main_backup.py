"""
guavacheck API

Platform Entry Point

Austin initializes before the API begins serving requests.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from backend.api.middleware.logging import LoggingMiddleware
from backend.api.middleware.security import SecurityMiddleware


from backend.austin.bootstrap import initialize

from backend.api.routes.health import router as health_router
from backend.api.routes.austin import router as austin_router
from backend.api.routes.engineering import router as engineering_router
from backend.api.routes.property import router as property_router
from backend.api.routes.verification import router as verification_router


@asynccontextmanager
async def lifespan(app: FastAPI):

    #
    # Austin Startup
    #

    initialize()

    yield

    print("Austin Shutdown Complete")


app = FastAPI(

    title="guavacheck API",

    version="1.0.0",

    lifespan=lifespan,

)

#
# Register Routes
#

app.include_router(health_router)

app.include_router(austin_router)

app.include_router(engineering_router)

app.include_router(property_router)

app.include_router(verification_router)

app.add_middleware(LoggingMiddleware)

app.add_middleware(SecurityMiddleware)

@app.get("/")
async def root():

    return {

        "platform": "guavacheck",

        "version": "1.0.0",

        "status": "online",

        "intelligence": "Austin",

    }