from app.core.payments.invoice_builder import InvoiceBuilder
from app.core.payments.payment_router import PaymentRouter
from app.core.payments.currency_guard import CurrencyGuard
from app.core.payments.payment_state import PaymentState
from app.core.integrations.payment_to_escrow_bridge import PaymentEscrowBridge

class PaymentEngine:

   def __init__(self):

    self.router = PaymentRouter()
    self.invoice_builder = InvoiceBuilder()
    self.state = PaymentState.INITIATED

    # NEW
    self.bridge = PaymentEscrowBridge() 

    # -------------------------
    # CREATE PAYMENT
    # -------------------------
    def create_payment(self, cost: dict, user: dict):

        currency = CurrencyGuard.normalize(cost.get("currency"))

        invoice = self.invoice_builder.build(
            amount=cost["estimated_cost"],
            currency=currency,
            user=user
        )

        self.state = PaymentState.PROCESSING

        return {
            "state": self.state,
            "invoice": invoice
        }

    # -------------------------
    # EXECUTE PAYMENT
    # -------------------------
    def execute_payment(self, invoice: dict, user: dict):

        result = self.router.charge(
            amount=invoice["amount"],
            currency=invoice["currency"],
            user=user
        )

        if result.get("status") == "success":
            self.state = PaymentState.SUCCESS
        else:
            self.state = PaymentState.FAILED

        return {
            "state": self.state,
            "provider_response": result
        }

    # -------------------------
    # FULL FLOW
    # -------------------------
    def process(self, cost: dict, user: dict, project: dict = None):

    invoice = self.create_payment(cost, user)

    payment_result = self.execute_payment(
        invoice["invoice"],
        user
    )

    # 🔗 AUTO ESCROW TRIGGER (NEW)
    escrow_result = None

    if project:
        escrow_result = self.bridge.trigger_from_payment(
            payment_result=payment_result,
            project=project,
            user=user
        )

    return {
        "invoice": invoice,
        "payment": payment_result,
        "escrow": escrow_result
    }
