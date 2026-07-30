from typing import Optional

from pydantic import BaseModel, ConfigDict


class RevisionCreate(BaseModel):
    render_id: str
    notes: Optional[str] = None


class RevisionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    render_id: str
    revision_number: int
    notes: Optional[str]
    image_url: Optional[str]