from app.core.escrow.fund_release_engine import FundReleaseEngine
from app.core.escrow.milestone_engine import MilestoneEngine


class ExecutionEscrowSync:
    def __init__(self):
        self.milestones = MilestoneEngine()
        self.fund_engine = FundReleaseEngine()

    def attach_project(self, escrow: dict, project: dict):
        escrow["milestones"] = self.milestones.generate(project.get("asset_type"))

        escrow["project"] = project

        return escrow

    def execute_phase(self, escrow: dict, phase_name: str):
        milestone = next(m for m in escrow["milestones"] if m["phase"] == phase_name)

        return self.fund_engine.release(escrow, milestone)
