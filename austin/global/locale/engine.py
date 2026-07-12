"""
Austin Locale Engine
"""

from __future__ import annotations


class LocaleEngine:
    """
    Locale intelligence.
    """

    def normalize(
        self,
        locale: str | None,
    ) -> str:

        if not locale:
            return "en-US"

        return locale.replace("_", "-")


locale_engine = LocaleEngine()