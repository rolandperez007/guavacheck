from app.core.escrow.execution_engine import EscrowExecutionEngine
from app.core.escrow.policy_engine import EscrowPolicyEngine


class AutonomousEscrow:
    def __init__(self):
        self.execution = EscrowExecutionEngine()
        self.policy = EscrowPolicyEngine()

    async def process(self, escrow_service, escrow_id, context=None, history=None):
        escrow = escrow_service.escrow.get_escrow(escrow_id)

        evaluation = await escrow_service.ai_evaluate(escrow_id, context, history)

        decision = evaluation["decision"]

        policy_check = self.policy.validate(escrow, decision)

        if not policy_check["approved"]:
            return {
                "status": "blocked",
                "reason": policy_check["reason"],
                "decision": decision,
            }

        result = self.execution.execute(escrow_service, escrow_id, decision)

        return {"status": "executed", "decision": decision, "result": result}
