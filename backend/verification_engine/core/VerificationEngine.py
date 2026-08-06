"""
guavacheck Verification Engine

Main orchestration engine.

Responsible for coordinating:

- Document verification
- Ownership checks
- Geospatial validation
- Fraud analysis
- Trust scoring
"""

from .VerificationConfig import VerificationConfig
from .VerificationModels import VerificationResult


class VerificationEngine:
    def __init__(self):

        self.name = VerificationConfig.ENGINE_NAME

        self.version = VerificationConfig.VERSION

    def verify_property(
        self,
        property_id,
        document_score=0,
        ownership_score=0,
        geospatial_score=0,
        fraud_score=0,
    ):

        result = VerificationResult(
            property_id=property_id,
            document_score=document_score,
            ownership_score=ownership_score,
            geospatial_score=geospatial_score,
            fraud_score=fraud_score,
        )

        result.final_score = self.calculate_score(result)

        result.status = self.determine_status(result.final_score)

        return result

    def calculate_score(self, result):

        score = (
            result.document_score * VerificationConfig.DOCUMENT_AUTHENTICITY_WEIGHT
            + result.ownership_score * VerificationConfig.OWNERSHIP_WEIGHT
            + result.geospatial_score * VerificationConfig.GEOSPATIAL_WEIGHT
            + result.fraud_score * VerificationConfig.FRAUD_WEIGHT
        )

        return round(score, 2)

    def determine_status(self, score):

        if score >= VerificationConfig.VERIFIED_THRESHOLD:
            return "VERIFIED"

        elif score >= VerificationConfig.REVIEW_THRESHOLD:
            return "UNDER_REVIEW"

        else:
            return "HIGH_RISK"

    def health_check(self):

        return {"engine": self.name, "version": self.version, "status": "ONLINE"}
