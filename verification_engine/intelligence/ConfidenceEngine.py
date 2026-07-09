"""
Confidence Engine

Calculates overall confidence
of verification.
"""


class ConfidenceEngine:

    def calculate(

        self,

        reasoning: dict,

        conflicts: dict,

    ) -> int:

        confidence = reasoning.get(

            "confidence",

            100,

        )

        if conflicts["has_conflicts"]:

            confidence -= 20

        return max(confidence, 0)
