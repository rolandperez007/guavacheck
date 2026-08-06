"""
Conversation Engine Manifest
"""

from .base import EngineManifest

MANIFEST = EngineManifest(
    name="conversation",
    version="1.0.0",
    description="General conversational intelligence.",
    engine_class=("backend.austin.engines.conversation.engine.ConversationEngine"),
    priority=100,
    intents=[
        "chat",
        "conversation",
    ],
    capabilities=[
        "conversation",
        "reasoning",
        "assistant",
    ],
    keywords=[
        "hello",
        "hi",
        "chat",
        "talk",
    ],
    tags=[
        "core",
        "default",
    ],
)
