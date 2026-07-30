from typing import Optional

from pydantic import BaseModel, ConfigDict


class MaterialCreate(BaseModel):
    room_id: str
    category: str
    name: str
    quantity: Optional[float] = None
    estimated_cost: Optional[float] = None


class MaterialResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    room_id: str
    category: str
    name: str
    quantity: Optional[float]
    estimated_cost: Optional[float]