"""
guavacheck Verification Engine

Trust Score Calculation Engine.

Creates a unified confidence score
for verified properties.
"""

from ..core.VerificationConfig import VerificationConfig


class TrustScoreEngine:
    def __init__(self):

        self.name = "guavacheck Trust Score Engine"

    def calculate(self, document_score, ownership_score, geospatial_score, fraud_score):

        score = (
            document_score * VerificationConfig.DOCUMENT_AUTHENTICITY_WEIGHT
            + ownership_score * VerificationConfig.OWNERSHIP_WEIGHT
            + geospatial_score * VerificationConfig.GEOSPATIAL_WEIGHT
            + fraud_score * VerificationConfig.FRAUD_WEIGHT
        )

        return {"trust_score": round(score, 2), "grade": self.generate_grade(score)}

    def generate_grade(self, score):

        if score >= 90:
            return "A+"

        if score >= 80:
            return "A"

        if score >= 70:
            return "B"

        if score >= 60:
            return "C"

        return "D"

    def health_check(self):

        return {"service": self.name, "status": "ONLINE"}
