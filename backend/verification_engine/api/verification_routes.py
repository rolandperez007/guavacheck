"""
guavacheck Verification Engine API

REST endpoints for property
verification operations.
"""


from fastapi import APIRouter

from ..core.VerificationEngine import (
    VerificationEngine
)


from ..fraud_detection.FraudDetector import (
    FraudDetector
)


from ..scoring.TrustScoreEngine import (
    TrustScoreEngine
)



router = APIRouter(
    prefix="/verification",
    tags=["Verification Engine"]
)



verification_engine = VerificationEngine()

fraud_detector = FraudDetector()

trust_engine = TrustScoreEngine()



@router.get("/health")
def health_check():

    return {

        "engine":
            verification_engine.health_check(),

        "fraud":
            fraud_detector.health_check()

    }



@router.post("/verify")
def verify_property(data: dict):


    result = verification_engine.verify_property(

        property_id=data.get(
            "property_id"
        ),

        document_score=data.get(
            "document_score",
            0
        ),

        ownership_score=data.get(
            "ownership_score",
            0
        ),

        geospatial_score=data.get(
            "geospatial_score",
            0
        ),

        fraud_score=data.get(
            "fraud_score",
            0
        )

    )


    return result



@router.post("/trust-score")
def generate_trust_score(data: dict):


    return trust_engine.calculate(

        document_score=data.get(
            "document_score",
            0
        ),

        ownership_score=data.get(
            "ownership_score",
            0
        ),

        geospatial_score=data.get(
            "geospatial_score",
            0
        ),

        fraud_score=data.get(
            "fraud_score",
            0
        )

    )