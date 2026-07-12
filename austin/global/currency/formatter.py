"""
Currency Formatter
"""

from __future__ import annotations

from .registry import CURRENCIES


class CurrencyFormatter:

    def format(
        self,
        amount: float,
        currency: str,
    ) -> str:

        currency = currency.upper()

        info = CURRENCIES.get(currency)

        if info is None:
            return f"{amount:,.2f}"

        symbol = info["symbol"]

        return f"{symbol}{amount:,.2f}"


formatter = CurrencyFormatter()