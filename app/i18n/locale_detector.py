import re


class LocaleDetector:
    COUNTRY_HINTS = {
        "nigeria": "NG",
        "usa": "US",
        "uk": "GB",
        "london": "GB",
        "dubai": "AE",
        "canada": "CA",
        "india": "IN",
    }

    @staticmethod
    def detect(text: str):
        text = text.lower()

        for key, value in LocaleDetector.COUNTRY_HINTS.items():
            if key in text:
                return {"country": value, "raw_match": key}

        return {"country": "GLOBAL", "raw_match": None}
