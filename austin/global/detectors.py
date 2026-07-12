"""
Austin Intelligence Detectors
"""

from __future__ import annotations

from .entities import COUNTRY_ALIASES
from .entities import CITY_ALIASES


class ContextDetectors:

    def detect_country(
        self,
        text: str,
    ) -> str | None:

        lower = text.lower()

        for keyword, country in COUNTRY_ALIASES.items():

            if keyword in lower:

                return country

        return None

    def detect_city(
        self,
        text: str,
    ) -> str | None:

        lower = text.lower()

        for keyword, city in CITY_ALIASES.items():

            if keyword in lower:

                return city

        return None

    def detect_currency(
        self,
        text: str,
    ) -> str | None:

        lower = text.lower()

        if "$" in lower or "usd" in lower:

            return "USD"

        if "€" in lower or "eur" in lower:

            return "EUR"

        if "£" in lower or "gbp" in lower:

            return "GBP"

        if "₦" in lower or "naira" in lower or "ngn" in lower:

            return "NGN"

        if "aed" in lower:

            return "AED"

        if "btc" in lower:

            return "BTC"

        return None


detectors = ContextDetectors()