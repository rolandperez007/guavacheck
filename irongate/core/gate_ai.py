from irongate.ai.context_builder import build_ai_context
from irongate.ai.risk_engine import compute_risk
from irongate.ai.decision_engine import make_decision
from irongate.ai.reputation import update_reputation


class IronGateAI:
    def __init__(self, rules):
        self.rules = rules

    def evaluate(self, context: dict):
        # 1. run traditional rules first
        for rule in self.rules:
            result = rule.evaluate(context)

            if isinstance(result, bool):
                if not result:
                    return "blocked:rule_failed"

            elif isinstance(result, str):
                return result

        # 2. build AI context
        ai_context = build_ai_context(context)

        # 3. compute risk
        risk = compute_risk(ai_context)

        # 4. decision
        decision = make_decision(risk)

        if decision == "block":
            return f"blocked:ai_risk_{risk}"

        if decision == "challenge":
            return f"challenge:ai_risk_{risk}"

        if decision == "block":
            update_reputation(context.get("user_id"), -10)
            return f"blocked:ai_risk_{risk}"

        if decision == "challenge":
            update_reputation(context.get("user_id"), -2)
            return f"challenge:ai_risk_{risk}"


# success path
update_reputation(context.get("user_id"), +1)
return True
