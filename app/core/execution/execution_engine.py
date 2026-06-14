from app.core.execution.task_generator import TaskGenerator
from app.core.execution.contractor_router import ContractorRouter
from app.core.execution.progress_tracker import ProgressTracker
from app.core.execution.execution_state import ExecutionState


class ExecutionEngine:
    def __init__(self):
        self.task_generator = TaskGenerator()
        self.contractor_router = ContractorRouter()
        self.progress_tracker = ProgressTracker()
        self.state = ExecutionState.PLANNED

    # -------------------------
    # CREATE EXECUTION PLAN
    # -------------------------
    def create_project(self, pipeline_result: dict):
        # 1. Generate Tasks
        task_data = self.task_generator.generate(pipeline_result)

        tasks = task_data["tasks"]

        # 2. Assign Contractors
        contractors = self.contractor_router.assign(tasks)

        # 3. Track Progress
        progress = self.progress_tracker.track(tasks)

        self.state = ExecutionState.IN_PROGRESS

        return {
            "state": self.state,
            "asset_type": task_data["asset_type"],
            "tasks": tasks,
            "contractors": contractors,
            "progress": progress,
        }

    # -------------------------
    # UPDATE STATUS
    # -------------------------
    def update_progress(self, completed_tasks: int, total_tasks: int):
        percent = (completed_tasks / total_tasks) * 100

        if percent == 100:
            self.state = ExecutionState.COMPLETED
        elif percent > 50:
            self.state = ExecutionState.IN_PROGRESS
        else:
            self.state = ExecutionState.BLOCKED

        return {"state": self.state, "progress_percent": percent}
