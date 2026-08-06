from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from app.institution.schemas import (
    BranchCreate,
    BranchRead,
    BranchUpdate,
)
from app.institution.services import InstitutionService

router = APIRouter(
    prefix="/{institution_id}/branches",
    tags=["Institution Branches"],
)


def get_service() -> InstitutionService:
    return InstitutionService()


@router.get(
    "/",
    response_model=list[BranchRead],
)
def list_branches(
    institution_id: UUID,
    service: InstitutionService = Depends(get_service),
):
    return service.list_branches(institution_id)


@router.post(
    "/",
    response_model=BranchRead,
    status_code=status.HTTP_201_CREATED,
)
def create_branch(
    institution_id: UUID,
    payload: BranchCreate,
    service: InstitutionService = Depends(get_service),
):
    return service.create_branch(
        institution_id,
        payload,
    )


@router.put(
    "/{branch_id}",
    response_model=BranchRead,
)
def update_branch(
    institution_id: UUID,
    branch_id: UUID,
    payload: BranchUpdate,
    service: InstitutionService = Depends(get_service),
):
    return service.update_branch(
        institution_id,
        branch_id,
        payload,
    )


@router.delete(
    "/{branch_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_branch(
    institution_id: UUID,
    branch_id: UUID,
    service: InstitutionService = Depends(get_service),
):
    service.delete_branch(
        institution_id,
        branch_id,
    )