"""
Enterprise Verification Rules

Each rule contributes to the final
Trust Score.
"""


class VerificationRules:

    TITLE_EXISTS = "Title Exists"

    OWNER_MATCH = "Owner Match"

    GOVERNOR_CONSENT = "Governor Consent"

    SURVEY_MATCH = "Survey Match"

    COORDINATE_MATCH = "Coordinate Match"

    REGISTRY_MATCH = "Registry Match"

    OCR_CONFIDENCE = "OCR Confidence"

    DOCUMENT_TAMPERING = "Document Tampering"

    FRAUD_DETECTED = "Fraud Detection"

    DUPLICATE_PROPERTY = "Duplicate Property"

    ACTIVE_LITIGATION = "Active Litigation"

    MORTGAGE_FLAG = "Mortgage Flag"

    PROPERTY_BLACKLIST = "Property Blacklist"

    SATELLITE_MATCH = "Satellite Match"

    CHAIN_OF_TITLE = "Chain Of Title"
