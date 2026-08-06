from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    full_name: str

    email: EmailStr

    password: str


class UserResponse(BaseModel):
    id: str

    full_name: str

    email: EmailStr

    is_verified: bool

    is_admin: bool

    class Config:
        from_attributes = True
