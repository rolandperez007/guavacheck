"""
Explanation Generator

Produces human-readable explanations describing
how a verification decision was reached.
"""

from typing import Dict, List


class ExplanationGenerator:

    """
    Converts technical verification results into
    understandable summaries.
    """

    def generate(

        self,

        verification: Dict,

    ) -> Dict:

        trust = verification.get(

            "trust_score",

            0,

        )

        confidence = verification.get(

            "confidence",

            0,

        )

        issues = verification.get(

            "issues",

            [],

        )

        evidence = verification.get(

            "evidence",

            [],

        )

        return {

            "summary": self.summary(

                trust,

                confidence,

            ),

            "strengths": self.strengths(

                evidence,

            ),

            "issues": self.describe_issues(

                issues,

            ),

            "recommendation": self.recommendation(

                trust,

                issues,

            ),

        }

    def summary(

        self,

        trust: float,

        confidence: float,

    ) -> str:

        return (

            f"The property achieved a trust score of "

            f"{trust:.2f} with an overall confidence "

            f"of {confidence:.2f}."

        )

    def strengths(

        self,

        evidence: List,

    ) -> List[str]:

        strengths = []

        for item in evidence:

            if item.get(

                "confidence",

                0,

            ) >= 0.90:

                strengths.append(

                    f"{item.get('source')} verified successfully."

                )

        return strengths

    def describe_issues(

        self,

        issues: List,

    ) -> List[str]:

        descriptions = []

        for issue in issues:

            descriptions.append(

                issue.get(

                    "message",

                    "Unknown verification issue.",

                )

            )

        return descriptions

    def recommendation(

        self,

        trust: float,

        issues: List,

    ) -> str:

        if trust >= 0.95:

            return "Verification passed with very high confidence."

        if trust >= 0.85:

            return "Property appears legitimate. Routine review recommended."

        if trust >= 0.70:

            return "Additional supporting documentation is recommended."

        if trust >= 0.50:

            return "Manual verification should be completed before proceeding."

        return "Do not rely on this verification until critical issues are resolved."