from app.core.payment_router import PaymentRouter
from app.core.wallet.wallet_engine import WalletEngine


class PaymentOrchestrator:
    def __init__(self):
        self.router = PaymentRouter()
        self.wallet = WalletEngine()

    def process_payment(self, amount, currency, user):
        payment = self.router.charge(amount=amount, currency=currency, user=user)

        # simulate successful payment
        if payment.get("status") == "initialized":
            self.wallet.credit(
                user_id=user["id"],
                amount=amount,
                currency=currency,
                source=payment["provider"],
            )

        return {"payment": payment, "wallet": self.wallet.get_wallet(user["id"])}
