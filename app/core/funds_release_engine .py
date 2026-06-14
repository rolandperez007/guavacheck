from app.core.escrow.escrow_state import EscrowState


class FundReleaseEngine:
    def release(self, escrow: dict, milestone: dict):
        amount = escrow["amount"] * milestone["percent"]

        escrow["released"] += amount
        escrow["balance"] -= amount

        escrow["state"] = EscrowState.PARTIALLY_RELEASED

        return {
            "released_amount": amount,
            "phase": milestone["phase"],
            "remaining_balance": escrow["balance"],
            "state": escrow["state"],
        }
