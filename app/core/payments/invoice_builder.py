import uuid


class InvoiceBuilder:
    def build(self, amount: float, currency: str, user: dict):
        return {
            "invoice_id": str(uuid.uuid4()),
            "amount": amount,
            "currency": currency,
            "user": user,
            "status": "generated",
        }
