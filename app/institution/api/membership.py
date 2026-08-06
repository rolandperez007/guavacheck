from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from app.institution.schemas import (
    MembershipCreate,
    MembershipRead,
)
from app.institution.services import MembershipService

router = APIRouter(
    prefix="/{institution_id}/members",
    tags=["Institution Membership"],
)


def get_service() -> MembershipService:
    return MembershipService()


@router.get(
    "/",
    response_model=list[MembershipRead],
)
def list_members(
    institution_id: UUID,
    service: MembershipService = Depends(get_service),
):
    return service.list_members(
        institution_id,
    )


@router.post(
    "/",
    response_model=MembershipRead,
    status_code=status.HTTP_201_CREATED,
)
def invite_member(
    institution_id: UUID,
    payload: MembershipCreate,
    service: MembershipService = Depends(get_service),
):
    return service.invite(
        institution_id,
        payload,
    )


@router.delete(
    "/{member_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def remove_member(
    institution_id: UUID,
    member_id: UUID,
    service: MembershipService = Depends(get_service),
):
    service.remove(
        institution_id,
        member_id,
    )