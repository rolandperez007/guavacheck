from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class BranchCreate(BaseModel):
    name: str
    code: str | None = None
    email: str | None = None
    phone: str | None = None
    country: str
    state: str | None = None
    city: str | None = None
    address: str | None = None


class BranchUpdate(BaseModel):
    name: str | None = None
    code: str | None = None
    email: str | None = None
    phone: str | None = None
    country: str | None = None
    state: str | None = None
    city: str | None = None
    address: str | None = None
    status: str | None = None


class BranchRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    institution_id: str
    name: str
    code: str | None = None
    email: str | None = None
    phone: str | None = None
    country: str
    state: str | None = None
    city: str | None = None
    address: str | None = None
    status: str
