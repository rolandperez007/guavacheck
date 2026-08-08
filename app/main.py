from fastapi import FastAPI

from app.config.settings import get_settings

from app.api.health import router as health_router
from app.api.database_health import router as database_router

from app.identity.api.router import router as identity_router
from app.users.api.router import router as users_router
from app.auth.api.router import router as auth_router


settings = get_settings()


app = FastAPI(
    title=settings.APP_NAME
)


app.include_router(
    health_router
)

app.include_router(
    database_router
)

app.include_router(
    identity_router
)

app.include_router(
    users_router
)

app.include_router(
    auth_router
)


@app.get("/")
def root():

    return {
        "application": settings.APP_NAME,
        "status": "running",
        "environment": settings.ENVIRONMENT
    }