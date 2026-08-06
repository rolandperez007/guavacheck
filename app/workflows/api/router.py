from fastapi import APIRouter

from .analytics_routes import router as analytics_router
from .event_routes import router as event_router
from .execution_routes import router as execution_router
from .history_routes import router as history_router
from .template_routes import router as template_router
from .validator_routes import router as validator_router
from .workflow_routes import router as workflow_router

router = APIRouter(
    prefix="/workflows",
    tags=["Workflow Engine"],
)

router.include_router(
    workflow_router,
)

router.include_router(
    execution_router,
)

router.include_router(
    template_router,
)

router.include_router(
    history_router,
)

router.include_router(
    analytics_router,
)

router.include_router(
    validator_router,
)

router.include_router(
    event_router,
)