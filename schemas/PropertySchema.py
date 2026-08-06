from pydantic import BaseModel


class PropertyCreate(BaseModel):
    title_number: str

    owner_name: str

    address: str

    latitude: float

    longitude: float


class PropertyResponse(PropertyCreate):
    id: str

    class Config:
        from_attributes = True
