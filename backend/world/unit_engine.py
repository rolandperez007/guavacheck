"""
Unit Engine
"""

from __future__ import annotations


class UnitEngine:
    def meters_to_feet(self, value: float) -> float:
        return value * 3.28084

    def feet_to_meters(self, value: float) -> float:
        return value / 3.28084


unit_engine = UnitEngine()
