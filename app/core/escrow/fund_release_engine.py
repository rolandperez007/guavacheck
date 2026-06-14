class FundReleaseEngine:
    def release(self, escrow: dict, milestone: dict):
        amount = escrow["amount"] * milestone["percent"]

        escrow["released"] += amount
        escrow["balance"] -= amount

        milestone["status"] = "released"

        return {
            "phase": milestone["phase"],
            "released_amount": amount,
            "remaining_balance": escrow["balance"],
            "status": "released",
        }
