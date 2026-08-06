from .base import EngineManifest

MANIFEST = EngineManifest(
    name="community",
    version="1.0.0",
    description="Community engine.",
    engine_class=("backend.austin.engines.community.engine.CommunityEngine"),
    priority=60,
    intents=[
        "community",
    ],
    capabilities=[
        "posts",
        "comments",
        "community",
    ],
)
