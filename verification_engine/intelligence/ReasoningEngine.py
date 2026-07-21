"""
Reasoning Engine

Coordinates all intelligence modules to produce
the final verification decision.
"""

from typing import Dict

from verification_engine.intelligence.EvidenceCollector import (
    EvidenceCollector,
)

from verification_engine.intelligence.ConfidenceEngine import (
    ConfidenceEngine,
)

from verification_engine.intelligence.ConflictResolver import (
    ConflictResolver,
)

from verification_engine.intelligence.ExplanationGenerator import (
    ExplanationGenerator,
)


class ReasoningEngine:
    """
    Primary AI reasoning engine.
    """

    def __init__(self):

        self.collector = EvidenceCollector()

        self.confidence = ConfidenceEngine()

        self.conflicts = ConflictResolver()

        self.explainer = ExplanationGenerator()

    def evaluate(
        self,
        evidence: Dict,
    ) -> Dict:

        confidence = self.confidence.calculate(
            evidence,
        )

        conflicts = self.conflicts.detect(
            evidence,
        )

        explanation = self.explainer.generate(
            confidence,
            conflicts,
        )

        return {

            "verified": (
                confidence["verified"]
                and not conflicts["conflict_found"]
            ),

            "confidence": confidence,

            "conflicts": conflicts,

            "explanation": explanation,

            "decision": (
                "VERIFIED"
                if confidence["verified"]
                and not conflicts["conflict_found"]
                else "REVIEW_REQUIRED"
            ),

        }