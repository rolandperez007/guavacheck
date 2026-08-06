from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from app.institution.schemas import SubscriptionRead
from app.institution.services import SubscriptionService

router = APIRouter(
    prefix="/{institution_id}/subscription",
    tags=["Institution Subscription"],
)


def get_service() -> SubscriptionService:
    return SubscriptionService()


@router.get(
    "/",
    response_model=SubscriptionRead,
)
def current_subscription(
    institution_id: UUID,
    service: SubscriptionService = Depends(get_service),
):
    return service.current(
        institution_id,
    )


@router.post(
    "/renew",
)
def renew_subscription(
    institution_id: UUID,
    service: SubscriptionService = Depends(get_service),
):
    return service.renew(
        institution_id,
    )


@router.post(
    "/cancel",
)
def cancel_subscription(
    institution_id: UUID,
    service: SubscriptionService = Depends(get_service),
):
    return service.cancel(
        institution_id,
    )