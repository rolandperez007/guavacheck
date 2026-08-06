"""
World Engine

Combines the existing global services into one execution context.
"""

from __future__ import annotations

from dataclasses import dataclass

from .currency_engine import currency_engine
from .language_engine import language_engine
from .locale_engine import locale_engine


@dataclass(slots=True)
class WorldContext:
    country: str

    language: str

    currency: str

    exchange_rate: float

    translated_query: str

    original_query: str


class WorldEngine:
    def build(
        self,
        *,
        query: str,
        country: str = "NG",
        language: str = "en",
        target_currency: str = "USD",
    ) -> WorldContext:

        locale = locale_engine.detect(country)

        translated = language_engine.translate(
            query,
            source_language=language,
            target_language="en",
        )

        rate = currency_engine.convert(
            amount=1,
            from_currency=locale.currency,
            to_currency=target_currency,
        )

        return WorldContext(
            country=country,
            language=language,
            currency=locale.currency,
            exchange_rate=rate.converted_amount,
            translated_query=translated.text,
            original_query=query,
        )


world_engine = WorldEngine()
