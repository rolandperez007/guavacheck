from typing import Optional

from pydantic import BaseModel, ConfigDict


class RenderCreate(BaseModel):
    project_id: str
    room_id: str
    provider: str = "openai"


class RenderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    project_id: str
    room_id: str
    provider: str
    image_url: Optional[str]
    status: str
    version: int