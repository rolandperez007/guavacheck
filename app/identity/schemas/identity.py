from datetime import datetime

from pydantic import BaseModel, EmailStr


class IdentityCreate(BaseModel):

    email: EmailStr

    phone: str | None = None

    identity_type: str = "individual"


class IdentityResponse(BaseModel):

    id: str

    email: EmailStr

    phone: str | None

    identity_type: str

    status: str

    created_at: datetime

    model_config = {
        "from_attributes": True
    }