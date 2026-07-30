from fastapi import APIRouter

from app.vision.api.projects import router as projects_router
from app.vision.api.rooms import router as rooms_router
from app.vision.api.renders import router as renders_router
from app.vision.api.furniture import router as furniture_router
from app.vision.api.materials import router as materials_router
from app.vision.api.revisions import router as revisions_router
from app.vision.api.exports import router as exports_router

router = APIRouter(
    prefix="/vision",
    tags=["Vision"],
)

router.include_router(projects_router)
router.include_router(rooms_router)
router.include_router(renders_router)
router.include_router(furniture_router)
router.include_router(materials_router)
router.include_router(revisions_router)
router.include_router(exports_router)