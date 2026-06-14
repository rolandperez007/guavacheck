from app.core.escrow.milestone_engine import MilestoneEngine
from app.core.escrow.fund_release_engine import FundReleaseEngine


class ExecutionEscrowSync:
    def __init__(self):
        self.milestone_engine = MilestoneEngine()
        self.release_engine = FundReleaseEngine()

    def attach_project(self, escrow: dict, project: dict):
        milestones = self.milestone_engine.generate(
            project.get("asset_type", "generic")
        )

        escrow["project"] = project
        escrow["milestones"] = milestones
        escrow["current_phase"] = 0

        return escrow

    def get_current_milestone(self, escrow: dict):
        phase = escrow.get("current_phase", 0)

        milestones = escrow.get("milestones", [])

        if phase >= len(milestones):
            return None

        return milestones[phase]

    def release_current_phase(self, escrow: dict):
        milestone = self.get_current_milestone(escrow)

        if not milestone:
            return {"status": "completed", "message": "All milestones completed"}

        result = self.release_engine.release(escrow, milestone)

        escrow["current_phase"] += 1

        return {
            "status": "released",
            "phase": milestone["phase"],
            "release": result,
            "next_phase": escrow["current_phase"],
        }

    def release_by_phase(self, escrow: dict, phase_name: str):
        milestone = next(
            (m for m in escrow["milestones"] if m["phase"] == phase_name), None
        )

        if not milestone:
            return {"status": "error", "message": f"Phase not found: {phase_name}"}

        return self.release_engine.release(escrow, milestone)
