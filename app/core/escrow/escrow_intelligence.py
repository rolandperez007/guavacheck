from app.core.router.model_gateway import ModelGateway


class EscrowIntelligence:

    def __init__(self):
    self.gateway = ModelGateway()
        
    async def evaluate(self, escrow: dict, context: dict = None, history: list = None):

        """
        Hybrid reasoning engine:
        rules + LLM + context memory
        """

        # -----------------------------
        # 1. BASE RULE SIGNALS
        # -----------------------------
        score = 0.5
        signals = []

        if escrow["status"] != "held":
            return {
                "action": "no_action",
                "confidence": 1.0,
                "reason": "invalid_state"
            }

        amount = escrow.get("amount", 0)

        if amount > 1_000_000:
            score -= 0.15
            signals.append("high_value_transaction")
        else:
            score += 0.1
            signals.append("standard_value")

        milestones = escrow.get("milestones", [])
        if len(milestones) == 0:
            score -= 0.2
            signals.append("missing_milestones")
        else:
            score += 0.15
            signals.append("milestones_defined")

        # -----------------------------
        # 2. CONTEXT SIGNALS
        # -----------------------------
        if context:
            if context.get("dispute_flag"):
                score -= 0.4
                signals.append("dispute_detected")

            if context.get("buyer_verified"):
                score += 0.1
                signals.append("buyer_verified")

            if context.get("seller_verified"):
                score += 0.1
                signals.append("seller_verified")

        # -----------------------------
        # 3. LLM REASONING LAYER
        # -----------------------------
        llm_prompt = f"""
You are Austin Escrow Intelligence v2.

Analyze this escrow transaction and decide risk level.

ESCROW DATA:
{escrow}

CONTEXT:
{context}

HISTORICAL SIGNALS:
{history}

Return:
- risk_score (0 to 1)
- recommendation: release | hold | refund
- reasoning bullets
"""

        try:
          
            llm_result = await self.gateway.ask(
                llm_prompt
            )

            llm_response = llm_result["response"]

        except Exception as e:
            llm_response = {
                "error": str(e)
            }

        # -----------------------------
        # 4. FINAL HYBRID DECISION
        # -----------------------------
        if score >= 0.75:
            action = "release"
        elif score <= 0.35:
            action = "refund"
        else:
            action = "hold"

        return {
            "action": action,
            "confidence": round(score, 2),
            "signals": signals,
            "llm_reasoning": llm_response,
            "recommended": True,
            "mode": "hybrid_ai_v2"
        }
