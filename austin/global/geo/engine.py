"""
Austin Geo Engine
"""

from __future__ import annotations

from .countries import COUNTRIES


class GeoEngine:
    """
    Country intelligence.
    """

    def country(self, name: str):

        return COUNTRIES.get(name)

    def exists(self, name: str) -> bool:

        return name in COUNTRIES

    def countries(self):

        return sorted(COUNTRIES.keys())


geo_engine = GeoEngine()