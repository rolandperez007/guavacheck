"""
Locale Engine
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Locale:
    country: str
    currency: str
    language: str
    timezone: str


class LocaleEngine:
    _countries = {
        "NG": Locale(
            country="Nigeria",
            currency="NGN",
            language="en",
            timezone="Africa/Lagos",
        ),
        "US": Locale(
            country="United States",
            currency="USD",
            language="en",
            timezone="America/New_York",
        ),
        "JP": Locale(
            country="Japan",
            currency="JPY",
            language="ja",
            timezone="Asia/Tokyo",
        ),
        "FR": Locale(
            country="France",
            currency="EUR",
            language="fr",
            timezone="Europe/Paris",
        ),
    }

    def detect(self, country_code: str) -> Locale:

        return self._countries.get(
            country_code.upper(),
            self._countries["US"],
        )


locale_engine = LocaleEngine()
