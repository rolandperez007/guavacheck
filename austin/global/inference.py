"""
Austin Context Inference Engine
"""

from __future__ import annotations

from .detectors import detectors
from .engine import global_engine


class ContextInferenceEngine:

    def infer(
        self,
        text: str,
    ):

        country = detectors.detect_country(text)

        if country is None:

            country = "United States"

        context = global_engine.build(

            country=country,

        )

        detected_currency = detectors.detect_currency(text)

        if detected_currency:

            context.metadata["requested_currency"] = detected_currency

        city = detectors.detect_city(text)

        if city:

            context.metadata["city"] = city

        context.metadata["original_query"] = text

        return context


context_inference_engine = ContextInferenceEngine()