from datetime import datetime
import json


def log_event(context, result):
    """Write a JSON-lines audit entry. Best-effort; never raise."""
    entry = {
        "ts": datetime.utcnow().isoformat(),
        "user_id": context.get("user_id"),
        "action": context.get("action"),
        "path": context.get("meta", {}).get("path") or context.get("path"),
        "method": context.get("meta", {}).get("method") or context.get("method"),
        "allowed": None,
        "score": None,
        "risk_score": None,
        "reason": None,
        "reasons": None,
        "decision": None,
        "decision_id": None,
        "rules_triggered": None,
        "final_action": None,
    }

    if isinstance(result, dict):
        entry["allowed"] = result.get("allowed")
        entry["score"] = result.get("score")
        entry["risk_score"] = result.get("score")
        entry["reason"] = result.get("reason")
        entry["reasons"] = result.get("reasons")
        entry["decision"] = result.get("decision")
        entry["decision_id"] = result.get("decision_id")
        entry["rules_triggered"] = result.get("rules_triggered")
        entry["final_action"] = result.get("final_action") or result.get("decision")
    else:
        entry["allowed"] = bool(result)
        entry["reason"] = str(result)

    try:
        with open("irongate_audit.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception:
        pass
