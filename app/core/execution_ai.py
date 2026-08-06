from app.core.execution_ai.milestone_detector import MilestoneDetector
from app.core.execution_ai.progress_analyzer import ProgressAnalyzer


class ExecutionAI:
    def __init__(self):
        self.analyzer = ProgressAnalyzer()
        self.detector = MilestoneDetector()

    def process_update(self, update: dict):
        analysis = self.analyzer.analyze(update)

        should_release = self.detector.should_release(analysis)

        return {
            "analysis": analysis,
            "release_funds": should_release,
            "reason": (
                "auto-detected milestone completion"
                if should_release
                else "milestone still in progress"
            ),
        }
