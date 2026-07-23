from .base import EngineManifest

MANIFEST = EngineManifest(
    name="finance",
    version="1.0",
    priority=80,
    engine_class="backend.austin.engines.finance.engine.FinanceEngine",
    description="Financial calculations.",
    capabilities=[
        "mortgage",
        "currency",
        "investment",
    ],
    intents=[
        "finance",
        "mortgage",
        "investment",
    ],
)