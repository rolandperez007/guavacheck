from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class VisionProjectCreate(BaseModel):
    name: str = Field(min_length=3, max_length=200)
    owner_id: str
    property_type: str
    design_style: str
    budget: Optional[int] = Field(default=None, ge=0)
    location: Optional[str] = None


class VisionProjectUpdate(BaseModel):
    name: Optional[str] = None
    design_style: Optional[str] = None
    budget: Optional[int] = Field(default=None, ge=0)
    location: Optional[str] = None
    status: Optional[str] = None


class VisionProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    name: str
    owner_id: str
    property_type: str
    design_style: str
    budget: Optional[int]
    location: Optional[str]
    status: str