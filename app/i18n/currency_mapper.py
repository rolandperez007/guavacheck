class CurrencyMapper:
    COUNTRY_CURRENCY = {
        "NG": "NGN",
        "US": "USD",
        "GB": "GBP",
        "AE": "AED",
        "CA": "CAD",
        "IN": "INR",
    }

    DEFAULT = "USD"

    @staticmethod
    def resolve(country: str):
        return CurrencyMapper.COUNTRY_CURRENCY.get(country, CurrencyMapper.DEFAULT)
