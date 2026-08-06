from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from app.institution.schemas import (
    InstitutionCreate,
    InstitutionRead,
    InstitutionUpdate,
)
from app.institution.services import InstitutionService

router = APIRouter()


def get_service() -> InstitutionService:
    """
    Temporary dependency.

    Later this will be replaced with
    dependency injection.
    """
    return InstitutionService()


@router.get(
    "/",
    response_model=list[InstitutionRead],
)
def list_institutions(
    service: InstitutionService = Depends(get_service),
):
    return service.list_all()


@router.get(
    "/{institution_id}",
    response_model=InstitutionRead,
)
def get_institution(
    institution_id: UUID,
    service: InstitutionService = Depends(get_service),
):
    institution = service.get(institution_id)

    if institution is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Institution not found.",
        )

    return institution


@router.post(
    "/",
    response_model=InstitutionRead,
    status_code=status.HTTP_201_CREATED,
)
def create_institution(
    payload: InstitutionCreate,
    service: InstitutionService = Depends(get_service),
):
    return service.create(payload)


@router.put(
    "/{institution_id}",
    response_model=InstitutionRead,
)
def update_institution(
    institution_id: UUID,
    payload: InstitutionUpdate,
    service: InstitutionService = Depends(get_service),
):
    return service.update(
        institution_id,
        payload,
    )


@router.delete(
    "/{institution_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_institution(
    institution_id: UUID,
    service: InstitutionService = Depends(get_service),
):
    service.delete(institution_id)