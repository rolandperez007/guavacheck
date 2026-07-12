"""
Localization Engine
"""

from __future__ import annotations

from .languages import LANGUAGES


class LocalizationEngine:
    """
    Detects and manages user language preferences.
    """

    def detect(self, language: str | None) -> str:

        if not language:
            return "en"

        language = language.lower()

        if language in LANGUAGES:
            return language

        return "en"

    def supported_languages(self):

        return LANGUAGES


localization_engine = LocalizationEngine()