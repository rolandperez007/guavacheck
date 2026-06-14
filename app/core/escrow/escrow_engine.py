
import uuid
from datetime import datetime
from app.core.events.event_bus import EventBus

class EscrowEngine:

    def __init__(self):
        self.escrows = {}
        self.events = EventBus()
    # -------------------------
    # STANDARD CREATE METHOD
    # -------------------------
    def create(
    self,
    amount: float,
    payer: str,
    payee: str,
    currency: str = "USD",
    asset_ref: str = None
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
    "updated_at": datetime.utcnow().isoformat()
}

    self.escrows[escrow_id] = escrow

    # ✅ EVENT EMIT AFTER CREATION
    if hasattr(self, "events"):
        self.events.emit("escrow.created", escrow)

    return escrow

    def get_escrow(self, escrow_id: str):
        return self.escrows.get(escrow_id, {"error": "not_found"})
        self.events.emit("escrow.created", escrow)
