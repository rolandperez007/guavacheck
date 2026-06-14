class ProgressAnalyzer:
    def analyze(self, update: dict):
        """
        update example:
        {
            "phase": "foundation",
            "progress_percent": 65,
            "notes": "steel framework ongoing"
        }
        """

        score = update.get("progress_percent", 0)

        status = "in_progress"

        if score >= 90:
            status = "near_complete"
        elif score >= 50:
            status = "in_progress"
        elif score < 50:
            status = "early_stage"

        return {
            "phase": update.get("phase"),
            "progress": score,
            "status": status,
            "risk_flag": score < 40,
        }
