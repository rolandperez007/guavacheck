"""
Country Profile
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CountryProfile:
    name: str

    code: str

    language: str

    locale: str

    currency: str

    timezone: str

    units: str

    measurement: str

    region: str
