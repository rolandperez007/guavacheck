class DisputeEngine:
    def open_dispute(self, escrow_id: str, reason: str):
        return {
            "escrow_id": escrow_id,
            "status": "disputed",
            "reason": reason,
            "action": "locked_for_review",
        }
