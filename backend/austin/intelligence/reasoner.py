"""
Austin Reasoner

Combines outputs from multiple engines.
"""

from __future__ import annotations


class AustinReasoner:
    def reason(
        self,
        plan,
        outputs: dict,
    ):

        return {
            "objective": plan.objective,
            "confidence": plan.confidence,
            "engines_used": list(outputs.keys()),
            "results": outputs,
        }


reasoner = AustinReasoner()
