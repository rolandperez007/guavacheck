from .base import EngineManifest

MANIFEST = EngineManifest(
    name="investor",
    version="1.0.0",
    description="Investor engine.",
    engine_class=("backend.austin.engines.investor.engine.InvestorEngine"),
    priority=75,
    intents=[
        "investment",
    ],
    capabilities=[
        "portfolio",
        "investment",
        "forecast",
    ],
)
