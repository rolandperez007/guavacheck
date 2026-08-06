"""
Austin Registry

Compatibility layer.

Actual engine registration lives inside EngineManager.
"""

from backend.engines.manager import engine_manager


class AustinRegistry:
    def register(self, engine):

        engine_manager.register(engine)

    def unregister(self, name):

        engine_manager.unregister(name)

    def get(self, name):

        return engine_manager.get(name)

    def exists(self, name):

        return engine_manager.exists(name)

    def list(self):

        return engine_manager.names()

    def enabled(self):

        return engine_manager.enabled()

    def count(self):

        return engine_manager.count()


registry = AustinRegistry()
