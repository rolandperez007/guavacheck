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

    def exists(self, name: str) -> bool:
        return name in self._engines

    def list(self):
        return list(self._engines.keys())

    def all(self):
        return list(self._engines.values())

    def enabled(self):
        return [
            e
            for e in self._engines.values()
            if getattr(e, "enabled", True)
        ]

    def healthy(self):
        return [
            e
            for e in self._engines.values()
            if getattr(e, "healthy", True)
        ]

    def count(self):
        return len(self._engines)

    def summary(self):
        return {
            "registered": self.count(),
            "healthy": len(self.healthy()),
            "enabled": len(self.enabled()),
        }


registry = EngineRegistry()