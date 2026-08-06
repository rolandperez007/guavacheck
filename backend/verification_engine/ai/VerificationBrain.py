"""
Verification Brain

Central AI coordinator for
property verification.
"""

from verification_engine.ai.FraudReasoner import FraudReasoner
from verification_engine.ai.TrustReasoner import TrustReasoner


class VerificationBrain:
    def __init__(self):

        self.fraud = FraudReasoner()

        self.trust = TrustReasoner()

    async def verify(
        self,
        verification_data,
    ):

        fraud = await self.fraud.analyze(verification_data)

        trust = await self.trust.calculate(fraud["fraud_score"])

        return {"fraud": fraud, "trust": trust, "approved": trust["trust_score"] >= 70}
