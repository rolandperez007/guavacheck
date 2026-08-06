from .base import EngineManifest

MANIFEST = EngineManifest(
    name="vision",
    version="1.0.0",
    description="Vision engine.",
    engine_class=("backend.austin.engines.vision.engine.VisionEngine"),
    priority=65,
    intents=[
        "vision",
        "image",
    ],
    capabilities=[
        "ocr",
        "image_analysis",
        "vision",
    ],
)
