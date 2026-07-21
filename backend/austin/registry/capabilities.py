"""
Austin Capabilities Registry

Maintains a registry of engine capabilities
for discovery, routing and AI planning.
"""

from __future__ import annotations

from typing import Dict, List


class CapabilityRegistry:

    def __init__(self) -> None:
        self._capabilities: Dict[str, List[str]] = {}

    def register(
        self,
        engine: str,
        capabilities: List[str],
    ) -> None:

        self._capabilities[engine] = capabilities

    def get(
        self,
        engine: str,
    ) -> List[str]:

        return self._capabilities.get(engine, [])

    def all(self) -> Dict[str, List[str]]:

        return dict(self._capabilities)


capability_registry = CapabilityRegistry()