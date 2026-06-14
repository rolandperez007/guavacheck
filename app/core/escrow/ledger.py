import uuid
from datetime import datetime


class Ledger:
    def __init__(self):
        self.records = []

    def log(self, action: str, data: dict):
        self.records.append(
            {
                "id": str(uuid.uuid4()),
                "action": action,
                "data": data,
                "timestamp": datetime.utcnow().isoformat(),
            }
        )

        return self.records[-1]
