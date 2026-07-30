from datetime import datetime

from pydantic import BaseModel, Field


class PropertyCreate(BaseModel):

    reference_code: str = Field(
        min_length=3,
        max_length=50
    )

    property_type: str = Field(
        min_length=2,
        max_length=50
    )

    status: str = Field(
        default="active"
    )

    country: str = Field(
        min_length=2,
        max_length=100
    )

    state: str = Field(
        min_length=2,
        max_length=100
    )

    city: str = Field(
        min_length=2,
        max_length=100
    )

    address: str = Field(
        min_length=5,
        max_length=255
    )

    latitude: float | None = None

    longitude: float | None = None

    created_by: str | None = None


class PropertyResponse(BaseModel):

    id: str

    reference_code: str

    property_type: str

    status: str

    country: str

    state: str

    city: str

    address: str

    latitude: float | None

    longitude: float | None

    created_by: str | None

    created_at: datetime

    updated_at: datetime


    class Config:

        from_attributes = True