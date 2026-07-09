from datetime import datetime

from pydantic import BaseModel


class OwnershipCreate(BaseModel):

    property_id: str

    owner_name: str

    acquisition_method: str

    acquisition_date: datetime | None = None


class OwnershipResponse(OwnershipCreate):

    id: str

    class Config:

        from_attributes = True