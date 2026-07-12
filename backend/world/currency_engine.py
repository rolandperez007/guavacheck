"""
Currency Engine

Provides lightweight currency conversion.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class CurrencyResult:
    from_currency: str
    to_currency: str
    rate: float
    converted_amount: float


class CurrencyEngine:

    _rates = {
        ("NGN", "USD"): 0.00065,
        ("USD", "NGN"): 1538.46,
        ("USD", "EUR"): 0.92,
        ("EUR", "USD"): 1.09,
        ("JPY", "USD"): 0.0068,
        ("USD", "JPY"): 147.0,
    }

    def convert(
        self,
        *,
        amount: float,
        from_currency: str,
        to_currency: str,
    ) -> CurrencyResult:

        if from_currency == to_currency:
            rate = 1.0
        else:
            rate = self._rates.get(
                (from_currency, to_currency),
                1.0,
            )

        return CurrencyResult(
            from_currency=from_currency,
            to_currency=to_currency,
            rate=rate,
            converted_amount=amount * rate,
        )


currency_engine = CurrencyEngine()