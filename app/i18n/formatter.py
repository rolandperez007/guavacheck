from .locale_detector import LocaleDetector
from .currency_mapper import CurrencyMapper
from .language_pack import LanguagePack
from .timezone_resolver import TimezoneResolver


class GlobalContext:
    @staticmethod
    def build(query: str):
        locale = LocaleDetector.detect(query)

        country = locale["country"]

        return {
            "country": country,
            "currency": CurrencyMapper.resolve(country),
            "language": LanguagePack.get_language(country),
            "timezone": TimezoneResolver.resolve(country),
            "locale_hint": locale,
        }
