"""
Reasoning Engine

Combines evidence into
AI reasoning.
"""


class ReasoningEngine:

    def reason(

        self,

        evidence: list,

    ) -> dict:

        confidence = 100

        issues = []

        for item in evidence:

            value = item.get("value", {})

            if isinstance(value, dict):

                if value.get("status") == "NOT_CONNECTED":

                    confidence -= 5

                    issues.append(

                        f"{item['source']} unavailable"

                    )

        return {

            "confidence": max(confidence, 0),

            "issues": issues,

            "recommendation": (

                "REVIEW"

                if confidence < 80

                else "VERIFY"

            )

        }
