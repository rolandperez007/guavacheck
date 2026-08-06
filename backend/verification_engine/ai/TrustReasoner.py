"""
Trust Score Engine
"""


class TrustReasoner:
    async def calculate(
        self,
        fraud_score,
    ):

        trust = max(0, 100 - fraud_score)

        return {"trust_score": trust}
