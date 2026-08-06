from .base import EngineManifest

MANIFEST = EngineManifest(
    name="engineering",
    version="1.0.0",
    description="Engineering engine.",
    engine_class=(
        "backend.engines.engineering.engine.EngineeringEngineEngineeringEngine"
    ),
    priority=95,
    intents=[
        "engineering",
        "construction",
        "building",
    ],
    capabilities=[
        "engineering",
        "calculations",
        "boq",
        "structural",
    ],
)
