"""
Austin Registry Health

Reports health information about
registered engines.
"""

from __future__ import annotations

from .registry import registry


class RegistryHealth:

    def status(self):

        return {
            "healthy": True,
            "registered_engines": registry.count(),
            "engines": registry.list(),
        }


registry_health = RegistryHealth()