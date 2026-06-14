"""Simple risk scoring helpers for IronGate.

Rules contribute items like {'action':'score','score':10,'reason':'...'}.
This module consolidates and clamps those into a 0-100 risk score.
"""


def compute_score(reasons: list) -> int:
    total = 0

    for r in reasons:
        try:
            if r.get("action") == "score":
                total += int(r.get("score", 0))
        except Exception:
            continue

    # clamp to 0-100
    if total < 0:
        total = 0
    if total > 100:
        total = 100

    return total
