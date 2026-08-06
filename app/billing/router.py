from fastapi import APIRouter, HTTPException

from app.billing.schemas import CheckoutResponse, PaymentCreate
from app.billing.service import create_checkout

router = APIRouter(prefix="/billing", tags=["Billing"])


@router.get("/health")
def billing_health():
    return {
        "service": "billing",
        "status": "online",
        "providers": {"stripe": "configured"},
    }


@router.post(
    "/checkout",
    response_model=CheckoutResponse,
)
def checkout(payment: PaymentCreate):

    try:
        session = create_checkout(payment)

        return {"success": True, "provider": payment.provider, **session}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
