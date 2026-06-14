from collections import defaultdict
from datetime import datetime

EVENT_LOG = []


def log_event(context, decision):
    EVENT_LOG.append(
        {
            "time": datetime.utcnow().isoformat(),
            "path": context.get("path"),
            "score": decision.get("score"),
            "decision": decision.get("decision"),
            "allowed": decision.get("allowed"),
        }
    )


def get_metrics():
    total = len(EVENT_LOG)
    blocked = len([e for e in EVENT_LOG if e["decision"] == "block"])
    warned = len([e for e in EVENT_LOG if e["decision"] == "warn"])

    return {
        "total_requests": total,
        "blocked": blocked,
        "warned": warned,
        "allow_rate": (total - blocked) / total if total else 1,
    }


def get_recent(limit=20):
    return EVENT_LOG[-limit:]
