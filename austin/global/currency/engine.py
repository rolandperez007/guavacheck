"""
Austin Currency Engine
"""

from __future__ import annotations

from .formatter import formatter
from .registry import CURRENCIES


class CurrencyEngine:
    """
    Currency intelligence.

    Exchange-rate providers will be plugged in later.
    """

    def supported(self):

        return CURRENCIES

    def exists(
        self,
        currency: str,
    ) -> bool:

        return currency.upper() in CURRENCIES

    def format(
        self,
        amount: float,
        currency: str,
    ) -> str:

        return formatter.format(amount, currency)

    def convert(
        self,
        amount: float,
        from_currency: str,
        to_currency: str,
    ) -> float:
        """
        Placeholder.

        Live FX integration will replace this implementation.
        """

        if from_currency.upper() == to_currency.upper():
            return amount

        return amount


currency_engine = CurrencyEngine()