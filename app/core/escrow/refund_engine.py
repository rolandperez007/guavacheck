class RefundEngine:
    def evaluate(self, escrow_state: str):
        if escrow_state == "disputed":
            return {"refund_allowed": True, "reason": "Dispute flagged"}

        if escrow_state == "created":
            return {"refund_allowed": True, "reason": "No funds released yet"}

        return {"refund_allowed": False, "reason": "Funds already released"}
