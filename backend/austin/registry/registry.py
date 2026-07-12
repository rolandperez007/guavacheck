"""
Austin Engine Registry
"""

from __future__ import annotations

from .engine import Engine


class EngineRegistry:

    def __init__(self):

        self._engines: dict[str, Engine] = {}

    def register(self, engine: Engine):

        self._engines[engine.name] = engine

    def unregister(self, name: str):

        self._engines.pop(name, None)

    def get(self, name: str):

        return self._engines.get(name)

    def all(self):

        return list(self._engines.values())

    def enabled(self):

        return [

            e

            for e in self._engines.values()

            if e.enabled

        ]

    def healthy(self):

        return [

            e

            for e in self._engines.values()

            if e.healthy

        ]

    def summary(self):

        return {

            "registered": len(self._engines),

            "healthy": len(self.healthy()),

            "enabled": len(self.enabled()),

        }


engine_registry = EngineRegistry()