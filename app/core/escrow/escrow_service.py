from app.core.wallet.wallet_engine import WalletEngine
from app.core.escrow.escrow_engine import EscrowEngine
from app.core.escrow.escrow_intelligence import EscrowIntelligence



class EscrowService:

    def __init__(self):
        self.wallet = WalletEngine()
        self.escrow = EscrowEngine()
        self.intelligence = EscrowIntelligence()

    def fund_escrow(self, buyer_id, seller_id, amount, currency, asset_ref):

        # 1. debit wallet first
        debit = self.wallet.debit(
            buyer_id,
            amount,
            currency,
            purpose="escrow_funding"
        )

        if isinstance(debit, dict) and "error" in debit:
            return debit

        # 2. create escrow record
        escrow = self.escrow.create_escrow(
            buyer_id,
            seller_id,
            amount,
            currency,
            asset_ref
        )

        return {
            "message": "escrow_funded",
            "escrow": escrow
        }

    def release(self, escrow_id):

        escrow = self.escrow.release_funds(escrow_id)

        return escrow

    def refund(self, escrow_id):

    escrow = self.escrow.get_escrow(escrow_id)

    if not escrow or "error" in escrow:
        return {"error": "escrow_not_found"}

    # ensure valid state
    if escrow["status"] != "held":
        return {
            "error": "invalid_refund_state",
            "status": escrow["status"]
        }
    async def ai_evaluate(self, escrow_id, context=None, history=None):

    escrow = self.escrow.get_escrow(escrow_id)

    if not escrow or "error" in escrow:
        return {"error": "escrow_not_found"}

    decision = await self.intelligence.evaluate(
        escrow,
        context,
        history
    )

    return {
        "escrow_id": escrow_id,
        "decision": decision
    }

    # 1. mark escrow refunded
    refunded = self.escrow.refund(escrow_id)

    if "error" in refunded:
        return refunded

    # 2. return money to wallet
    self.wallet.credit(
        user_id=escrow["buyer_id"],
        amount=escrow["amount"],
        currency=escrow["currency"],
        source="escrow_refund"
    )

    return {
        "message": "refund_successful",
        "escrow": refunded,
        "wallet_updated": True
    }
