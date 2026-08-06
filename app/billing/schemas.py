from pydantic import BaseModel


class PaymentCreate(BaseModel):
    provider: str = "stripe"
    amount: int
    currency: str
    description: str


class CheckoutResponse(BaseModel):
    success: bool
    provider: str
    session_id: str
    checkout_url: str
