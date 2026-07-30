from typing import Optional

from pydantic import BaseModel, Field


class PropertyPassportCreate(BaseModel):

    property_name: str = Field(
        min_length=2,
        max_length=200,
    )

    property_type: str = Field(
        min_length=2,
        max_length=100,
    )

    owner_id: str

    country: str

    state: str

    city: str

    address: str

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    construction_year: Optional[int] = None

    land_area: Optional[float] = None

    building_area: Optional[float] = None


class PropertyPassportUpdate(BaseModel):

    property_name: Optional[str] = None

    property_type: Optional[str] = None

    country: Optional[str] = None

    state: Optional[str] = None

    city: Optional[str] = None

    address: Optional[str] = None

    latitude: Optional[float] = None

    longitude: Optional[float] = None

    construction_year: Optional[int] = None

    land_area: Optional[float] = None

    building_area: Optional[float] = None


class PropertyPassportResponse(BaseModel):

    id: str

    passport_id: str

    property_name: str

    property_type: str

    owner_id: str

    country: str

    state: str

    city: str

    address: str

    latitude: Optional[float]

    longitude: Optional[float]

    construction_year: Optional[int]

    land_area: Optional[float]

    building_area: Optional[float]

    verified: bool

    dna_generated: bool

    twin_generated: bool

    published: bool

    class Config:
        from_attributes = True