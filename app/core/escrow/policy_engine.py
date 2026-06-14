class EscrowPolicyEngine:
    def validate(self, escrow, decision):
        amount = escrow.get("amount", 0)

        confidence = decision.get("confidence", 0)

        action = decision.get("action")

        if amount > 100000:
            return {"approved": False, "reason": "manual_review_required"}

        if confidence < 0.75:
            return {"approved": False, "reason": "low_confidence"}

        return {"approved": True, "reason": "policy_passed"}
