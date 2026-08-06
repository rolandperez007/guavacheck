from pydantic import BaseModel, ConfigDict


class FurnitureCreate(BaseModel):
    room_id: str
    category: str
    name: str
    quantity: float = 1
    estimated_cost: float | None = None


class FurnitureResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    room_id: str
    category: str
    name: str
    quantity: float
    estimated_cost: float | None
