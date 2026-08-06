from .base import EngineManifest

MANIFEST = EngineManifest(
    name="property",
    version="1.0.0",
    priority=90,
    engine_class="backend.engines.property.engine.PropertyEngine",
    description="Property intelligence engine.",
    capabilities=[
        "property_search",
        "valuation",
        "ownership",
        "verification",
    ],
    intents=[
        "property",
        "valuation",
        "ownership",
    ],
)
