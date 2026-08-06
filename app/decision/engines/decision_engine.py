from app.decision.models.context import DecisionContext
from app.decision.models.report import DecisionReport


class DecisionEngine:
    def evaluate(
        self,
        context: DecisionContext,
    ) -> DecisionReport:

        report = DecisionReport()

        # ---------------------------------------------------
        # Passport
        # ---------------------------------------------------

        if context.passport:
            report.recommendations.append("Property Passport available.")

            report.score += 10

        # ---------------------------------------------------
        # Vision
        # ---------------------------------------------------

        if context.vision:
            report.recommendations.append("Vision render completed.")

            report.score += 10

        # ---------------------------------------------------
        # Twin
        # ---------------------------------------------------

        if context.twin:
            report.recommendations.append("Digital Twin is active.")

            report.score += 10

        report.confidence = report.score / 30

        return report
