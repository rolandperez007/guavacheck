from fastapi import APIRouter

from .branch import router as branch_router
from .membership import router as membership_router
from .institution import router as institution_router
from .subscription import router as subscription_router
from .verification import router as verification_router

router = APIRouter(
    prefix="/institutions",
    tags=["Institutions"],
)

router.include_router(
    institution_router,
)

router.include_router(
    branch_router,
)

router.include_router(
    membership_router,
)

router.include_router(
    subscription_router,
)

router.include_router(
    verification_router,
)