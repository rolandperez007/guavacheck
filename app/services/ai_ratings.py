from irongate.core.rating_engine import build_ai_status
from irongate.bootstrap import gate


def get_system_snapshot():
    """
    Single source of truth for Guava AI + Austin ratings.
    """

    context = {"path": "/dashboard/summary", "body": {}, "headers": {}}

    result = gate.evaluate(context)
    score = result.get("score", 0)

    guava_ai = build_ai_status("guava_ai", score)
    austin = build_ai_status("austin", score)

    return {
        "guava_ai": guava_ai.__dict__,
        "austin": austin.__dict__,
        "raw_score": score,
        "decision": result.get("decision"),
        "rules_triggered": result.get("rules_triggered", []),
        "risk": result.get("final_action"),
    }
