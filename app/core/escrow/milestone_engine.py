class MilestoneEngine:
    def generate(self, asset_type="generic"):
        return [
            {"phase": "foundation", "percent": 0.20, "status": "pending"},
            {"phase": "structure", "percent": 0.30, "status": "pending"},
            {"phase": "roofing", "percent": 0.20, "status": "pending"},
            {"phase": "finishing", "percent": 0.20, "status": "pending"},
            {"phase": "handover", "percent": 0.10, "status": "pending"},
        ]
