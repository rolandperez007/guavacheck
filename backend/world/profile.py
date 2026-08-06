"""
World Profile

Represents the detected global profile
for a user or request.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class WorldProfile:
    country: str

    language: str

    currency: str

    timezone: str

    unit_system: str

    locale: str

    region: str
