"""
guavacheck Verification Engine

Risk Analysis Engine.

Converts verification signals into
property risk intelligence.
"""


class RiskAnalyzer:
    def __init__(self):

        self.name = "guavacheck Risk Analyzer"

    def evaluate(self, verification_result):

        score = verification_result.final_score

        risk_level = self.calculate_level(score)

        return {
            "trust_score": score,
            "risk_level": risk_level,
            "recommendation": self.recommendation(risk_level),
        }

    def calculate_level(self, score):

        if score >= 85:
            return "LOW_RISK"

        elif score >= 60:
            return "MEDIUM_RISK"

        return "HIGH_RISK"

    def recommendation(self, level):

        recommendations = {
            "LOW_RISK": "Property passed initial verification.",
            "MEDIUM_RISK": "Additional checks recommended.",
            "HIGH_RISK": "Do not proceed without further investigation.",
        }

        return recommendations.get(level)
