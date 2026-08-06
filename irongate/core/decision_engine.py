from dataclasses import dataclass


@dataclass
class RuleSignal:
    name: str
    score: int = 0
    critical: bool = False
    reason: str | None = None


@dataclass
class DecisionResult:
    allowed: bool
    decision: str  # allow | warn | block
    score: int
    reasons: list[str]
    rules_triggered: list[dict]
    final_action: str


class DecisionEngine:
    def __init__(self, warn_threshold=50, block_threshold=80):
        self.warn_threshold = warn_threshold
        self.block_threshold = block_threshold

    def evaluate(self, signals: list[RuleSignal]) -> DecisionResult:
        score = 0
        reasons = []
        triggered = []
        critical_block = False

        for s in signals:
            score += s.score

            triggered.append(
                {"rule": s.name, "weight": s.score, "critical": s.critical}
            )

            if s.reason:
                reasons.append(s.reason)

            if s.critical and s.score > 0:
                critical_block = True

        # FINAL DECISION LOGIC (ONLY PLACE THAT MATTERS)
        if critical_block:
            return DecisionResult(
                allowed=False,
                decision="block",
                score=score,
                reasons=reasons,
                rules_triggered=triggered,
                final_action="block",
            )

        if score >= self.block_threshold:
            return DecisionResult(
                allowed=False,
                decision="block",
                score=score,
                reasons=reasons,
                rules_triggered=triggered,
                final_action="block",
            )

        if score >= self.warn_threshold:
            return DecisionResult(
                allowed=True,
                decision="warn",
                score=score,
                reasons=reasons,
                rules_triggered=triggered,
                final_action="warn",
            )

        return DecisionResult(
            allowed=True,
            decision="allow",
            score=score,
            reasons=reasons,
            rules_triggered=triggered,
            final_action="allow",
        )
