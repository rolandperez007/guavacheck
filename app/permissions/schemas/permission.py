from datetime import datetime

from pydantic import BaseModel


class PermissionCreate(BaseModel):

    name: str

    resource: str

    action: str



class PermissionResponse(BaseModel):

    id: str

    name: str

    resource: str

    action: str

    created_at: datetime


    model_config = {
        "from_attributes": True
    }