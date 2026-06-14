from datetime import datetime


class EscrowV2:
    def __init__(self, payment_router):
        self.router = payment_router
        self.escrows = {}

    # -----------------------------
    # CREATE ESCROW
    # -----------------------------
    def create_escrow(self, project_id: str, total: float, currency: str, user: dict):
        escrow = {
            "project_id": project_id,
            "status": "active",
            "total": total,
            "currency": currency,
            "user": user,
            "created_at": datetime.utcnow().isoformat(),
            "released": 0,
            "milestones": [],
            "refund_status": None,
        }

        self.escrows[project_id] = escrow
        return escrow

    # -----------------------------
    # ADD MILESTONE
    # -----------------------------
    def add_milestone(self, project_id: str, name: str, pct: float):
        escrow = self.escrows.get(project_id)

        if not escrow:
            return {"error": "escrow_not_found"}

        amount = escrow["total"] * pct

        escrow["milestones"].append(
            {"name": name, "amount": amount, "status": "locked"}
        )

        return escrow

    # -----------------------------
    # RELEASE PAYMENT
    # -----------------------------
    def release(self, project_id: str, milestone_name: str):
        escrow = self.escrows.get(project_id)

        if not escrow:
            return {"error": "escrow_not_found"}

        for m in escrow["milestones"]:
            if m["name"] == milestone_name and m["status"] == "locked":
                m["status"] = "released"
                escrow["released"] += m["amount"]

                return self.router.charge(
                    amount=m["amount"], currency=escrow["currency"], user=escrow["user"]
                )

        return {"error": "invalid_milestone"}

    # -----------------------------
    # REFUND ENGINE (NEW)
    # -----------------------------
    def refund(self, project_id: str, reason: str):
        escrow = self.escrows.get(project_id)

        if not escrow:
            return {"error": "escrow_not_found"}

        if escrow["released"] > 0:
            refund_amount = escrow["total"] - escrow["released"]
        else:
            refund_amount = escrow["total"]

        escrow["status"] = "refunded"
        escrow["refund_status"] = reason

        return {
            "status": "refund_processed",
            "amount": refund_amount,
            "currency": escrow["currency"],
            "reason": reason,
        }

    # -----------------------------
    # DISPUTE FLAGGING
    # -----------------------------
    def dispute(self, project_id: str, issue: str):
        escrow = self.escrows.get(project_id)

        if not escrow:
            return {"error": "escrow_not_found"}

        escrow["status"] = "disputed"

        return {
            "status": "dispute_opened",
            "project_id": project_id,
            "issue": issue,
            "action": "manual_review_required",
        }
