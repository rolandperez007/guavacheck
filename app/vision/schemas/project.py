from pydantic import BaseModel, ConfigDict, Field


class VisionProjectCreate(BaseModel):
    name: str = Field(min_length=3, max_length=200)
    owner_id: str
    property_type: str
    design_style: str
    budget: int | None = Field(default=None, ge=0)
    location: str | None = None


class VisionProjectUpdate(BaseModel):
    name: str | None = None
    design_style: str | None = None
    budget: int | None = Field(default=None, ge=0)
    location: str | None = None
    status: str | None = None


class VisionProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    owner_id: str
    property_type: str
    design_style: str
    budget: int | None
    location: str | None
    status: str
