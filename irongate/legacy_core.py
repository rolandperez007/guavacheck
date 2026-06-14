from irongate.scoring import compute_score


class IronGate:
    def __init__(self, score_threshold: int = 50):
        self.rules = []
        self.score_threshold = score_threshold

    def register_rule(self, rule):
        self.rules.append(rule)

    def evaluate(self, context):
        """Evaluate context against registered rules.

        Rules may return:
        - True: pass
        - {'action':'block','reason':..., 'priority':'critical'|'soft'}
        - {'action':'score','score':int, 'reason':...}

        Returns a dict: {allowed: bool, reason: str|None, risk_score: int, reasons: list}
        """
        reasons = []
        raw_reasons = []

        for rule in self.rules:
            try:
                res = rule(context)
            except Exception as e:
                # Treat exceptions as soft warnings
                raw = {"action": "error", "reason": str(e), "priority": "soft"}
                raw_reasons.append(raw)
                continue

            if res is True:
                continue

            if res is False:
                # legacy boolean false => critical block
                return {
                    "allowed": False,
                    "reason": "Blocked by rule",
                    "risk_score": 100,
                    "reasons": [
                        {
                            "action": "block",
                            "reason": "rule returned False",
                            "priority": "critical",
                        }
                    ],
                }

            if isinstance(res, dict):
                raw_reasons.append(res)

                action = res.get("action")
                priority = res.get("priority", "soft")

                if action == "block" and priority == "critical":
                    # immediate critical block
                    return {
                        "allowed": False,
                        "reason": res.get("reason"),
                        "risk_score": 100,
                        "reasons": raw_reasons,
                    }
                # otherwise just collect and score later

        # compute total risk score
        score = compute_score(raw_reasons)

        allowed = score < self.score_threshold

        reason = None if allowed else "risk threshold exceeded"

        return {
            "allowed": allowed,
            "reason": reason,
            "risk_score": score,
            "reasons": raw_reasons,
        }
