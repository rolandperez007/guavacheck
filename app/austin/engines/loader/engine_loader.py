"""
Austin Engine Loader

Registers Austin-compatible
engines into the runtime.
"""

from app.austin.runtime.router import EngineRegistry


class EngineLoader:

    def __init__(self):
        self.registry = EngineRegistry()

    def register(
        self,
        engine,
    ):
        self.registry.register(
            engine.name,
            engine,
        )

    def registry_summary(self):
        return self.registry.summary()

    def get_registry(self):
        return self.registry