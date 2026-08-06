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

    latitude: float | None = None

    longitude: float | None = None

    construction_year: int | None = None

    land_area: float | None = None

    building_area: float | None = None


class PropertyPassportUpdate(BaseModel):
    property_name: str | None = None

    property_type: str | None = None

    country: str | None = None

    state: str | None = None

    city: str | None = None

    address: str | None = None

    latitude: float | None = None

    longitude: float | None = None

    construction_year: int | None = None

    land_area: float | None = None

    building_area: float | None = None


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

    latitude: float | None

    longitude: float | None

    construction_year: int | None

    land_area: float | None

    building_area: float | None

    verified: bool

    dna_generated: bool

    twin_generated: bool

    published: bool

    class Config:
        from_attributes = True
