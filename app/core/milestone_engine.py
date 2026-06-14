from datetime import datetime, timedelta


class MilestoneEngine:
    def generate(self, project: dict):
        asset = project.get("asset_type", "unknown")

        base_plan = self._base_milestones(asset)

        return {
            "project_type": asset,
            "created_at": datetime.utcnow().isoformat(),
            "milestones": base_plan,
        }

    def _base_milestones(self, asset_type: str):
        if asset_type in ["hotel", "hospital", "school"]:
            return [
                {"stage": "design", "duration_weeks": 4, "payment_pct": 0.1},
                {"stage": "foundation", "duration_weeks": 6, "payment_pct": 0.2},
                {"stage": "structure", "duration_weeks": 10, "payment_pct": 0.3},
                {"stage": "finishing", "duration_weeks": 8, "payment_pct": 0.25},
                {"stage": "handover", "duration_weeks": 2, "payment_pct": 0.15},
            ]

        return [
            {"stage": "planning", "duration_weeks": 2, "payment_pct": 0.2},
            {"stage": "execution", "duration_weeks": 6, "payment_pct": 0.6},
            {"stage": "handover", "duration_weeks": 2, "payment_pct": 0.2},
        ]
