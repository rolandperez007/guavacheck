from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class InstitutionCreate(BaseModel):
    legal_name: str
    display_name: str
    institution_type: str
    registration_number: str
    tax_id: str | None = None
    logo_url: str | None = None
    website: str | None = None
    email: str
    phone: str | None = None
    country: str
    state: str | None = None
    city: str | None = None
    address: str | None = None


class InstitutionUpdate(BaseModel):
    legal_name: str | None = None
    display_name: str | None = None
    institution_type: str | None = None
    registration_number: str | None = None
    tax_id: str | None = None
    logo_url: str | None = None
    website: str | None = None
    email: str | None = None
    phone: str | None = None
    country: str | None = None
    state: str | None = None
    city: str | None = None
    address: str | None = None
    status: str | None = None
    verification_status: str | None = None


class InstitutionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    legal_name: str
    display_name: str
    institution_type: str
    registration_number: str
    tax_id: str | None = None
    logo_url: str | None = None
    website: str | None = None
    email: str
    phone: str | None = None
    country: str
    state: str | None = None
    city: str | None = None
    address: str | None = None
    verification_status: str
    status: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class SubscriptionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    institution_id: str
    tier: str
    plan_name: str
    active: bool
    auto_renew: bool
    starts_at: datetime
    expires_at: datetime | None = None
    renews_at: datetime | None = None
