class MilestoneDetector:
    def should_release(self, analysis: dict):
        if analysis["progress"] >= 90 and not analysis["risk_flag"]:
            return True

        return False
