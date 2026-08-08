from fastapi import APIRouter

from app.config.settings import get_settings


router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


settings = get_settings()


@router.get("/")
def health_check():

    return {
        "status": "healthy",
        "application": settings.APP_NAME,
        "environment": settings.ENVIRONMENT
    }