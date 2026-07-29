from pydantic import BaseModel


class TwinCreate(BaseModel):
    property_id: str
    owner_id: str


class TwinResponse(BaseModel):
    id: str
    property_id: str
    owner_id: str
    status: str
    version: int

    class Config:
        from_attributes = True