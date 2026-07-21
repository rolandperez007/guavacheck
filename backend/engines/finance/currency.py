"""
GuavaCheck Finance Currency Module

Global currency intelligence layer.

Responsibilities:
- currency conversion
- supported currency registry
- crypto readiness
- exchange metadata
"""


from typing import Dict, Any


class CurrencyEngine:

    name = "currency"


    def __init__(self):

        self.supported_currencies = {

            "NGN": {
                "country": "Nigeria",
                "type": "fiat",
            },

            "USD": {
                "country": "United States",
                "type": "fiat",
            },

            "EUR": {
                "country": "European Union",
                "type": "fiat",
            },

            "GBP": {
                "country": "United Kingdom",
                "type": "fiat",
            },

            "KES": {
                "country": "Kenya",
                "type": "fiat",
            },

            "AED": {
                "country": "United Arab Emirates",
                "type": "fiat",
            },

            "BTC": {
                "country": "Global",
                "type": "crypto",
            },

            "ETH": {
                "country": "Global",
                "type": "crypto",
            },

        }


    def list_supported(self) -> Dict[str, Any]:

        return {

            "currencies": self.supported_currencies,

            "count": len(
                self.supported_currencies
            ),

            "status": "READY",

        }


    def convert(
        self,
        amount: float,
        from_currency: str,
        to_currency: str,
        rate: float | None = None,
    ) -> Dict[str, Any]:
        """
        Currency conversion.

        External exchange providers can later
        replace the placeholder rate layer.
        """

        if from_currency not in self.supported_currencies:

            return {

                "status": "ERROR",

                "message": (
                    f"Unsupported currency: {from_currency}"
                ),

            }


        if to_currency not in self.supported_currencies:

            return {

                "status": "ERROR",

                "message": (
                    f"Unsupported currency: {to_currency}"
                ),

            }


        if rate is None:

            rate = 1.0


        return {

            "status": "SUCCESS",

            "amount": amount,

            "from": from_currency,

            "to": to_currency,

            "converted_amount": amount * rate,

            "rate_used": rate,

        }