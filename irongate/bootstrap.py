from irongate.core.gate_v2 import IronGateV2


# Define rules (you can extend later)
def auth_rule(context):
    if not context.get("api_key"):
        return "missing api key"
    return True


rules = [
    {"rule": auth_rule, "weight": 50, "critical": False, "rule__name": "auth_rule"}
]

# SINGLE GLOBAL GATE INSTANCE
gate = IronGateV2(rules=rules, score_threshold=100, warn_threshold=50)
