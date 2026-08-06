from pydantic import BaseModel


class VerificationRequest(BaseModel):
    property_id: str


class VerificationResponse(BaseModel):
    verification_id: str

    trust_score: int

    status: str

    certificate_id: str | None = None

    class Config:
        from_attributes = True
