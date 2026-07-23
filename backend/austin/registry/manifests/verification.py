from .base import EngineManifest

MANIFEST = EngineManifest(

    name="verification",

    version="1.0.0",

    description="Property verification engine.",

    engine_class=(
        "backend.austin.engines.verification.engine."
        "VerificationEngine"
    ),

    priority=98,

    intents=[
        "verification",
        "verify",
    ],

    capabilities=[
        "property_verification",
        "fraud_detection",
        "ownership_validation",
    ],
)