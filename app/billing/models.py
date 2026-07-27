from datetime import datetime
from uuid import uuid4


class Payment:

    def __init__(
        self,
        user_id: str,
        amount: int,
        currency: str,
        provider: str,
        description: str | None = None
    ):
        self.id = str(uuid4())
        self.user_id = user_id
        self.amount = amount
        self.currency = currency
        self.provider = provider
        self.description = description
        self.status = "pending"
        self.created_at = datetime.utcnow()