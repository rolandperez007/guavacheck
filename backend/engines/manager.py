"""
Engine Manager

Single source of truth for all platform engines.

Austin does not maintain its own registry.

Austin queries EngineManager.
"""

from __future__ import annotations

from typing import Dict, List

from .base import BaseEngine


class EngineManager:

    def __init__(self):

        self._engines: Dict[str, BaseEngine] = {}

    # -------------------------------------------------
    # Registration
    # -------------------------------------------------

    def register(self, engine: BaseEngine):

        self._engines[engine.name] = engine

    def unregister(self, name: str):

        self._engines.pop(name, None)

    # -------------------------------------------------
    # Lookup
    # -------------------------------------------------

    def get(self, name: str):

        return self._engines.get(name)

    def exists(self, name: str):

        return name in self._engines

    def all(self):

        return self._engines

    def names(self) -> List[str]:

        return sorted(self._engines.keys())

    def enabled(self):

        return [

            engine

            for engine in self._engines.values()

            if engine.enabled

        ]

    # -------------------------------------------------
    # Diagnostics
    # -------------------------------------------------

    async def health(self):

        report = {}

        for engine in self._engines.values():

            report[engine.name] = await engine.health()

        return report

    def count(self):

        return len(self._engines)


engine_manager = EngineManager()