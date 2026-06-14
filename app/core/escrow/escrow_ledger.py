import json
import os
from datetime import datetime
import uuid


class EscrowLedger:
    def __init__(self, path="data/escrow_ledger.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump([], f)

    # -----------------------------
    # LOAD / SAVE
    # -----------------------------
    def _load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    # -----------------------------
    # EVENT CREATION
    # -----------------------------
    def emit(self, event_type: str, escrow_id: str, payload: dict):
        ledger = self._load()

        event = {
            "event_id": str(uuid.uuid4()),
            "event_type": event_type,
            "escrow_id": escrow_id,
            "payload": payload,
            "timestamp": datetime.utcnow().isoformat(),
        }

        ledger.append(event)
        self._save(ledger)

        return event

    # -----------------------------
    # GET EVENTS FOR ESCROW
    # -----------------------------
    def get_events(self, escrow_id: str):
        ledger = self._load()

        return [e for e in ledger if e["escrow_id"] == escrow_id]

    # -----------------------------
    # REBUILD STATE FROM EVENTS
    # -----------------------------
    def rebuild(self, escrow_id: str):
        events = self.get_events(escrow_id)

        if not events:
            return None

        state = {
            "escrow_id": escrow_id,
            "balance": 0,
            "released": 0,
            "status": "unknown",
            "milestones": [],
        }

        for e in events:
            t = e["event_type"]
            p = e["payload"]

            if t == "escrow_created":
                state.update(p)

            elif t == "milestone_added":
                state["milestones"].append(p)

            elif t == "funds_released":
                state["released"] += p["amount"]
                state["balance"] -= p["amount"]

            elif t == "refund_processed":
                state["status"] = "refunded"

            elif t == "escrow_funded":
                state["status"] = "funded"

        return state
