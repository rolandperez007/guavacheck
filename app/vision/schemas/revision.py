from pydantic import BaseModel, ConfigDict


class RevisionCreate(BaseModel):
    render_id: str
    notes: str | None = None


class RevisionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    render_id: str
    revision_number: int
    notes: str | None
    image_url: str | None
