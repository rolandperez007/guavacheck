"""
Austin Engine Registry
"""

from __future__ import annotations

from backend.austin.engines.conversation.engine import conversation_engine


class EngineRegistry:

    def __init__(self):

        self._engines = {}

    def register(self, engine):

        self._engines[engine.name] = engine

    def get(self, name):

        return self._engines.get(name)

    def registered(self):

        return sorted(self._engines.keys())


registry = EngineRegistry()

registry.register(conversation_engine)