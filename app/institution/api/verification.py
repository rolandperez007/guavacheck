from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends

from app.institution.services import VerificationService

router = APIRouter(
    prefix="/{institution_id}/verification",
    tags=["Institution Verification"],
)


def get_service() -> VerificationService:
    return VerificationService()


@router.get(
    "/status",
)
def status(
    institution_id: UUID,
    service: VerificationService = Depends(get_service),
):
    return service.status(
        institution_id,
    )


@router.post(
    "/submit",
)
def submit(
    institution_id: UUID,
    service: VerificationService = Depends(get_service),
):
    return service.submit(
        institution_id,
    )


@router.post(
    "/approve",
)
def approve(
    institution_id: UUID,
    service: VerificationService = Depends(get_service),
):
    return service.approve(
        institution_id,
    )


@router.post(
    "/reject",
)
def reject(
    institution_id: UUID,
    reason: str,
    service: VerificationService = Depends(get_service),
):
    return service.reject(
        institution_id,
        reason,
    )