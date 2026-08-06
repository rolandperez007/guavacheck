"""
guavacheck Verification Engine
Configuration Layer

Controls verification thresholds,
engine modes and scoring parameters.
"""


class VerificationConfig:
    ENGINE_NAME = "guavacheck Verification Engine"
    VERSION = "1.0.0"

    # Verification confidence thresholds

    VERIFIED_THRESHOLD = 85
    REVIEW_THRESHOLD = 60
    HIGH_RISK_THRESHOLD = 40

    # Document confidence

    DOCUMENT_AUTHENTICITY_WEIGHT = 0.30

    OWNERSHIP_WEIGHT = 0.30

    GEOSPATIAL_WEIGHT = 0.20

    FRAUD_WEIGHT = 0.20

    # Supported document categories

    SUPPORTED_DOCUMENTS = [
        "certificate_of_occupancy",
        "deed_of_assignment",
        "deed_of_conveyance",
        "survey_plan",
        "gazette",
        "allocation_letter",
        "building_approval",
        "tax_document",
    ]

    # Engine modes

    MODE_BASIC = "basic"
    MODE_ADVANCED = "advanced"
    MODE_GOVERNMENT = "government"

    DEFAULT_MODE = MODE_BASIC

    @classmethod
    def get_engine_info(cls):

        return {
            "name": cls.ENGINE_NAME,
            "version": cls.VERSION,
            "mode": cls.DEFAULT_MODE,
        }
