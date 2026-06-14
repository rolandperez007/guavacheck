from app.core.execution_engine_v2 import ExecutionEngineV2
from app.core.escrow.escrow_engine import EscrowEngine
from app.core.intelligence.execution_intelligence_v1 import ExecutionIntelligenceV1
from app.core.project_pipeline import ProjectPipeline


class ExecutionEscrowSyncV3:
    def __init__(self):
        self.execution_engine = ExecutionEngineV2()
        self.escrow_engine = EscrowEngine()
        self.intelligence = ExecutionIntelligenceV1()
        self.pipeline_engine = ProjectPipeline()

    # -----------------------------
    # MAIN ORCHESTRATION FLOW
    # -----------------------------
    def create_project_with_escrow(self, query: str, user: dict):
        # 1. Pipeline
        pipeline = self.pipeline_engine.run(query)

        # 2. Execution
        execution = self.execution_engine.create_project_execution(pipeline)

        cost = pipeline["cost"]

        # 3. Escrow (IMPORTANT: use create NOT create_escrow)
        escrow = self.escrow_engine.create(
            amount=cost["estimated_cost"],
            payer="client",
            payee="contractor",
            currency=cost.get("currency", "USD"),
            asset_ref=execution["execution_id"],
        )

        # 4. FIXED INTELLIGENCE CALL (ONLY ONE ARG)
        intelligence = self.intelligence.analyze(execution)

        return {"execution": execution, "escrow": escrow, "intelligence": intelligence}

    # -----------------------------
    # ESCROW FLOW
    # -----------------------------
    def release_next_phase(self, escrow: dict):
        return self.execution_engine.release_next_phase(escrow)
