import json
import os
from datetime import datetime


class EscrowStore:
    def __init__(self, path="data/escrows.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)

        if not os.path.exists(self.path):
            with open(self.path, "w") as f:
                json.dump({}, f)

    def _load(self):
        with open(self.path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, "w") as f:
            json.dump(data, f, indent=2)

    def save_escrow(self, escrow):
        data = self._load()

        data[escrow["escrow_id"]] = escrow
        escrow["updated_at"] = datetime.utcnow().isoformat()

        self._save(data)

        return escrow

    def get_escrow(self, escrow_id):
        data = self._load()

        return data.get(escrow_id)

    def update_escrow(self, escrow_id, updates: dict):
        data = self._load()

        if escrow_id not in data:
            return None

        data[escrow_id].update(updates)
        data[escrow_id]["updated_at"] = datetime.utcnow().isoformat()

        self._save(data)

        return data[escrow_id]

    def get_all(self):
        return self._load()
