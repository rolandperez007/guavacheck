import uuid
from datetime import datetime


class EscrowEngine:
    def __init__(self):
        self.escrows = {}
        self.events = None  # optional event bus hook

    def set_event_bus(self, event_bus):
        self.events = event_bus

    # -------------------------
    # CREATE ESCROW (CLEAN)
    # -------------------------
    def create(
        self,
        amount: float,
        payer: str,
        payee: str,
        currency: str = "USD",
        asset_ref: str = None,
    ):
        escrow_id = str(uuid.uuid4())

        escrow = {
            "escrow_id": escrow_id,
            "amount": amount,
            "currency": currency.upper(),
            "payer": payer,
            "payee": payee,
            "asset_ref": asset_ref,
            "balance": amount,
            "released": 0,
            "status": "funded",
            "milestones": [],
            "current_phase": 0,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat(),
        }

        # store first (IMPORTANT)
        self.escrows[escrow_id] = escrow

        # emit event AFTER object exists
        if self.events:
            self.events.emit("escrow.created", escrow)

        return escrow

    # -------------------------
    # GET ESCROW
    # -------------------------
    def get_escrow(self, escrow_id: str):
        return self.escrows.get(escrow_id, {"error": "not_found"})
