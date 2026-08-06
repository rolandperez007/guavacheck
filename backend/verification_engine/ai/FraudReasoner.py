"""
Fraud Reasoner

Combines evidence from
OCR, Registry,
GIS and Documents.
"""


class FraudReasoner:
    async def analyze(
        self,
        verification_data,
    ):

        score = 0

        reasons = []

        if verification_data.get("title_valid") is False:
            score += 40

            reasons.append("Invalid Title")

        if verification_data.get("owner_verified") is False:
            score += 30

            reasons.append("Owner mismatch")

        if verification_data.get("coordinates_valid") is False:
            score += 20

            reasons.append("Coordinate mismatch")

        return {"fraud_score": score, "reasons": reasons}
