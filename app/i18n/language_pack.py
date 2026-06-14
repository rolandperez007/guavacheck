class LanguagePack:
    SUPPORTED_LANGS = {
        "NG": "en",
        "US": "en",
        "GB": "en",
        "AE": "en",
        "IN": "en",
        "FR": "fr",
        "ES": "es",
        "DE": "de",
    }

    @staticmethod
    def get_language(country: str):
        return LanguagePack.SUPPORTED_LANGS.get(country, "en")
