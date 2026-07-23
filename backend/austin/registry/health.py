"""
Austin Registry Health
"""

from __future__ import annotations

from datetime import datetime

from backend.austin.registry.registry import registry


class RegistryHealth:

    def report(self) -> dict:

        return {

            "timestamp": datetime.utcnow(),

            "healthy": registry.booted,

            "engine_count": registry.count(),

            "engines": registry.list_engines(),

            "details": registry.health(),

        }


registry_health = RegistryHealth()