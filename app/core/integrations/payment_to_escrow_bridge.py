from app.core.escrow.escrow_engine import EscrowEngine


class PaymentEscrowBridge:
    def __init__(self):
        self.escrow = EscrowEngine()

    # -----------------------------
    # AUTO ESCROW ACTIVATION
    # -----------------------------
    def trigger_from_payment(self, payment_result: dict, project: dict, user: dict):
        # 1. CHECK PAYMENT SUCCESS
        payment_status = payment_result.get("state")

        if payment_status != "success":
            return {"status": "skipped", "reason": "payment_not_successful"}

        # 2. EXTRACT COST
        cost = project.get("cost", {})
        amount = cost.get("estimated_cost", 0)
        currency = cost.get("currency", "USD")

        # 3. CREATE ESCROW
        escrow = self.escrow.create(
            amount=amount,
            payer=user,
            payee={"system": "guava_execution_layer"},
            currency=currency,
        )

        return {
            "status": "escrow_activated",
            "escrow": escrow,
            "linked_payment": payment_result,
        }
