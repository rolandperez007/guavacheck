from pydantic import BaseModel, ConfigDict


class RoomCreate(BaseModel):
    project_id: str
    name: str
    room_type: str
    width: float | None = None
    length: float | None = None
    height: float | None = None


class RoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    project_id: str
    name: str
    room_type: str
    width: float | None
    length: float | None
    height: float | None
