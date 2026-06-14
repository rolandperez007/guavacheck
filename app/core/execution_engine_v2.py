from app.core.escrow.escrow_engine import EscrowEngine
from app.core.escrow.execution_sync import ExecutionEscrowSync


class ExecutionEngineV2:
    def __init__(self):
        self.escrow = EscrowEngine()

        self.sync = ExecutionEscrowSync()

    def create_project_execution(self, pipeline_result):
        cost = pipeline_result["cost"]

        escrow = self.escrow.create(
            amount=cost["estimated_cost"],
            payer="client",
            payee="contractor",
            currency=cost.get("currency", "USD"),
        )

        escrow = self.sync.attach_project(escrow, pipeline_result["project"])

        return {"execution_id": escrow["escrow_id"], "escrow": escrow}

    def release_next_phase(self, escrow):
        return self.sync.release_current_phase(escrow)
