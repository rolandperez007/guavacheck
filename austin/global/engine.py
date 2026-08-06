"""
Austin Global Intelligence Engine

Combines all intelligence engines into one execution context.
"""

from __future__ import annotations

from .context import GlobalContext
from .currency.engine import currency_engine
from .geo.engine import geo_engine
from .i18n.engine import localization_engine
from .locale.engine import locale_engine


class GlobalEngine:
    """
    Builds the GlobalContext used by Austin.
    """

    def build(
        self,
        *,
        country: str = "United States",
        language: str | None = None,
    ) -> GlobalContext:

        profile = geo_engine.country(country)

        if profile is None:
            profile = geo_engine.country("United States")

        detected_language = localization_engine.detect(language or profile["language"])

        locale = locale_engine.normalize(profile["locale"])

        return GlobalContext(
            language=detected_language,
            locale=locale,
            country=country,
            currency=profile["currency"],
            timezone=profile["timezone"],
            units=profile["units"],
            measurement=profile["measurement"],
            region=profile["region"],
            metadata={
                "currency_supported": currency_engine.exists(profile["currency"]),
            },
        )


global_engine = GlobalEngine()
