from datetime import datetime
import uuid


class WalletEngine:
    def __init__(self):
        # simple in-memory store (later DB)
        self.wallets = {}

    def _create_wallet(self, user_id: str):
        self.wallets[user_id] = {
            "user_id": user_id,
            "balance": {"USD": 0.0, "NGN": 0.0, "EUR": 0.0, "GBP": 0.0},
            "transactions": [],
        }

    def get_wallet(self, user_id: str):
        if user_id not in self.wallets:
            self._create_wallet(user_id)

        return self.wallets[user_id]

    def credit(self, user_id: str, amount: float, currency: str, source: str):
        wallet = self.get_wallet(user_id)

        currency = currency.upper()

        wallet["balance"][currency] += amount

        wallet["transactions"].append(
            {
                "id": str(uuid.uuid4()),
                "type": "credit",
                "amount": amount,
                "currency": currency,
                "source": source,
                "timestamp": datetime.utcnow().isoformat(),
            }
        )

        return wallet

    def debit(self, user_id: str, amount: float, currency: str, purpose: str):
        wallet = self.get_wallet(user_id)

        currency = currency.upper()

        if wallet["balance"][currency] < amount:
            return {
                "error": "insufficient_funds",
                "balance": wallet["balance"][currency],
            }

        wallet["balance"][currency] -= amount

        wallet["transactions"].append(
            {
                "id": str(uuid.uuid4()),
                "type": "debit",
                "amount": amount,
                "currency": currency,
                "purpose": purpose,
                "timestamp": datetime.utcnow().isoformat(),
            }
        )

        return wallet

    def get_balance(self, user_id: str):
        return self.get_wallet(user_id)["balance"]
