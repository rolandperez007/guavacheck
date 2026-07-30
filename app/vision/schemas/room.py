from typing import Optional

from pydantic import BaseModel, ConfigDict


class RoomCreate(BaseModel):
    project_id: str
    name: str
    room_type: str
    width: Optional[float] = None
    length: Optional[float] = None
    height: Optional[float] = None


class RoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    project_id: str
    name: str
    room_type: str
    width: Optional[float]
    length: Optional[float]
    height: Optional[float]