class MilestoneExecutor:
    def __init__(self, escrow_engine=None):
        self.escrow = escrow_engine

    def execute_milestone(self, stage: int, task: str):
        if self.escrow:
            self.escrow.release(stage)

        return {
            "milestone": stage,
            "task": task,
            "status": "executed",
            "payment_triggered": self.escrow is not None,
        }
