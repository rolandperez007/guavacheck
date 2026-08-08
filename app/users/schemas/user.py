from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):

    identity_id: str

    username: str | None = None

    password: str



class UserResponse(BaseModel):

    id: str

    identity_id: str

    username: str | None

    status: str

    created_at: datetime


    model_config = {
        "from_attributes": True
    }