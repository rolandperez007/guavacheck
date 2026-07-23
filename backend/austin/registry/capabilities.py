"""
Austin Capability Registry

Provides capability-based discovery for Austin engines.
"""

from __future__ import annotations

from backend.austin.registry.registry import registry


class CapabilityRegistry:
    """
    Capability lookup service.
    """

    def find(
        self,
        capability: str,
    ) -> list[object]:

        return registry.find_by_capability(
            capability
        )

    def supports(
        self,
        capability: str,
    ) -> bool:

        return bool(
            registry.find_by_capability(
                capability
            )
        )

    def intents(
        self,
        intent: str,
    ) -> list[object]:

        return registry.find_by_intent(
            intent
        )

    def engines(self) -> list[str]:

        return registry.list_engines()


capability_registry = CapabilityRegistry()