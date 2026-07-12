"""
Timezone Engine
"""

from __future__ import annotations


class TimezoneEngine:

    def timezone_for_country(self, country: str) -> str:

        mapping = {
            "NG": "Africa/Lagos",
            "US": "America/New_York",
            "JP": "Asia/Tokyo",
            "FR": "Europe/Paris",
        }

        return mapping.get(country.upper(), "UTC")


timezone_engine = TimezoneEngine()