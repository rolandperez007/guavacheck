"""
Geo Engine
"""

from __future__ import annotations


class GeoEngine:
    def detect_country(self, latitude: float, longitude: float) -> str:
        return "NG"


geo_engine = GeoEngine()
