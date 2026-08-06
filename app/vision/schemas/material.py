from pydantic import BaseModel, ConfigDict


class MaterialCreate(BaseModel):
    room_id: str
    category: str
    name: str
    quantity: float | None = None
    estimated_cost: float | None = None


class MaterialResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    room_id: str
    category: str
    name: str
    quantity: float | None
    estimated_cost: float | None
