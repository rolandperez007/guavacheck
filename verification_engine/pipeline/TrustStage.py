"""
Trust Stage

Calculates trust indicators before
the AI reasoning engine evaluates
the verification package.
"""


class TrustStage:
    name = "TRUST"

    async def execute(
        self,
        context,
    ):

        score = 0

        #
        # Evidence sources
        #

        document_result = context.stages.get("DOCUMENT", {})

        government_result = context.stages.get("GOVERNMENT", {})

        registry_result = context.stages.get("REGISTRY", {})

        fraud_result = context.stages.get("FRAUD", {})

        rule_result = context.stages.get("RULE_ENGINE", {})

        #
        # Document confidence
        #

        if document_result.get("documents_valid"):
            score += 20

        #
        # Government intelligence
        #

        if government_result.get("status") == "INTELLIGENCE_READY":
            score += 25

        #
        # Registry verification
        #

        if registry_result.get("completed"):
            score += 25

        #
        # Rule engine
        #

        if rule_result.get("verification_ready"):
            score += 20

        #
        # Fraud adjustment
        #

        risk = fraud_result.get("risk_score", 0)

        score -= risk / 2

        #
        # Clamp score
        #

        score = max(0, min(100, round(score, 2)))

        if score >= 90:
            trust_level = "VERIFIED"

        elif score >= 75:
            trust_level = "HIGH_CONFIDENCE"

        elif score >= 50:
            trust_level = "REVIEW_REQUIRED"

        else:
            trust_level = "HIGH_RISK"

        result = {
            "completed": True,
            "trust_score": score,
            "trust_level": trust_level,
            "status": "CALCULATED",
        }

        context.trust_score = score

        context.stages[self.name] = result

        context.evidence.append({"type": "trust_calculation", "data": result})

        return context
