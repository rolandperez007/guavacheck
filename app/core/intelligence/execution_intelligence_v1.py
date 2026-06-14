from datetime import datetime


class ExecutionIntelligenceV1:
    def analyze(self, execution: dict):
        escrow = execution.get("escrow", {})
        milestones = escrow.get("milestones", [])

        total = len(milestones)
        completed = len([m for m in milestones if m.get("status") == "released"])
        pending = total - completed

        # -----------------------------
        # PROGRESS SCORE
        # -----------------------------
        progress_score = 0

        if total > 0:
            progress_score = completed / total

        # -----------------------------
        # RISK ENGINE
        # -----------------------------
        risk_score = 0.0

        # risk increases if no progress but money released
        if escrow.get("released", 0) > 0 and completed == 0:
            risk_score += 0.4

        # risk increases if many pending milestones
        if pending > completed:
            risk_score += 0.2

        # risk increases if project is early but large fund locked
        if escrow.get("balance", 0) > escrow.get("amount", 1) * 0.8:
            risk_score += 0.1

        # clamp risk
        risk_score = min(risk_score, 1.0)

        # -----------------------------
        # HEALTH STATUS
        # -----------------------------
        if risk_score < 0.3:
            status = "healthy"
        elif risk_score < 0.7:
            status = "watch"
        else:
            status = "critical"

        # -----------------------------
        # ESTIMATED DELAY SIGNAL
        # -----------------------------
        delay_signal = "none"

        if status == "watch":
            delay_signal = "possible_delay"
        elif status == "critical":
            delay_signal = "high_delay_risk"

        # -----------------------------
        # FINAL INTELLIGENCE REPORT
        # -----------------------------
        return {
            "timestamp": datetime.utcnow().isoformat(),
            "progress_score": round(progress_score, 2),
            "risk_score": round(risk_score, 2),
            "status": status,
            "delay_signal": delay_signal,
            "milestone_summary": {
                "total": total,
                "completed": completed,
                "pending": pending,
            },
            "recommendation": self._recommend(status),
        }

    def _recommend(self, status: str):
        if status == "healthy":
            return "continue_execution"
        elif status == "watch":
            return "monitor_closely"
        else:
            return "intervene_or_audit"
