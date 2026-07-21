"""
Austin Engine Discovery

Provides discovery services for all
registered Austin engines.
"""

from __future__ import annotations

from .registry import registry


class EngineDiscovery:

    def names(self):

        return registry.list()

    def exists(
        self,
        name: str,
    ) -> bool:

        return registry.exists(name)

    def count(self) -> int:

        return registry.count()


engine_discovery = EngineDiscovery()