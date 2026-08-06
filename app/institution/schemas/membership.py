from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class MembershipCreate(BaseModel):
    user_id: str
    role: str = "staff"
    branch_id: str | None = None
    job_title: str | None = None
    department: str | None = None
    is_primary_contact: bool = False
    is_active: bool = True


class MembershipUpdate(BaseModel):
    role: str | None = None
    branch_id: str | None = None
    job_title: str | None = None
    department: str | None = None
    is_primary_contact: bool | None = None
    is_active: bool | None = None


class MembershipRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    institution_id: str
    user_id: str
    role: str
    branch_id: str | None = None
    job_title: str | None = None
    department: str | None = None
    invitation_status: str
    is_primary_contact: bool
    is_active: bool
