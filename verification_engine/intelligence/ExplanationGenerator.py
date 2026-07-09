"""
Explanation Generator

Produces human-readable
verification reports.
"""


class ExplanationGenerator:

    def generate(

        self,

        reasoning: dict,

        confidence: int,

    ) -> str:

        lines = []

        lines.append(

            f"Confidence Score: {confidence}%"

        )

        lines.append("")

        for issue in reasoning["issues"]:

            lines.append(f"- {issue}")

        lines.append("")

        lines.append(

            f"Recommendation: {reasoning['recommendation']}"

        )

        return "\n".join(lines)
