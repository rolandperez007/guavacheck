class CurrencyGuard:
    SUPPORTED = ["USD", "NGN", "GBP", "EUR", "AED", "CAD", "INR"]

    @staticmethod
    def normalize(currency: str):
        if not currency:
            return "USD"

        currency = currency.upper()

        return currency if currency in CurrencyGuard.SUPPORTED else "USD"
