"""
Confidence Engine

Calculates the overall confidence score for
a property verification using evidence from
every stage of the verification pipeline.
"""

from typing import Dict, List


class ConfidenceEngine:

    """
    Produces a confidence score between
    0.0 and 1.0.
    """

    def __init__(self):

        self.weights = {

            "documents": 0.25,

            "registry": 0.25,

            "geospatial": 0.20,

            "timeline": 0.10,

            "fraud": 0.15,

            "rules": 0.05,

        }

    def calculate(

        self,

        evidence: Dict,

    ) -> Dict:

        scores = {}

        weighted_total = 0.0

        for category, weight in self.weights.items():

            value = float(

                evidence.get(category, 0)

            )

            scores[category] = value

            weighted_total += value * weight

        confidence = round(

            min(max(weighted_total, 0.0), 1.0),

            4,

        )

        return {

            "confidence": confidence,

            "weights": self.weights,

            "scores": scores,

            "status": self.classify(confidence),

        }

    def classify(

        self,

        score: float,

    ) -> str:

        if score >= 0.95:

            return "VERY_HIGH"

        if score >= 0.85:

            return "HIGH"

        if score >= 0.70:

            return "MEDIUM"

        if score >= 0.50:

            return "LOW"

        return "VERY_LOW"

    def merge(

        self,

        values: List[float],

    ) -> float:

        if not values:

            return 0.0

        return round(

            sum(values) / len(values),

            4,

        )