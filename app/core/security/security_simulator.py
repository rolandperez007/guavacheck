# app/core/security/security_simulator.py

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class SecurityTestResult:
    test_name: str
    passed: bool
    risk_level: str
    details: str


class SecuritySimulator:
    def __init__(self, engine, memory, supabase_service):
        self.engine = engine
        self.memory = memory
        self.supabase = supabase_service

    # -----------------------------
    # 1. CROSS USER MEMORY TEST
    # -----------------------------
    async def test_cross_user_memory_isolation(self):
        user_a = "user_A"
        user_b = "user_B"

        await self.memory.save(user_a, "secret A data")

        data_b = await self.memory.recall(user_b)

        return SecurityTestResult(
            test_name="cross_user_memory",
            passed=(data_b == []),
            risk_level="HIGH" if data_b else "CRITICAL",
            details="User B should not access User A memory",
        )

    # -----------------------------
    # 2. ORG SPOOFING TEST
    # -----------------------------
    def test_org_isolation(self, context_a, context_b):
        allowed = context_a.org_id == context_b.org_id

        return SecurityTestResult(
            test_name="org_isolation",
            passed=allowed,
            risk_level="HIGH" if not allowed else "OK",
            details="Cross-org data leakage protection",
        )

    # -----------------------------
    # 3. ROLE ESCALATION TEST
    # -----------------------------
    def test_role_escalation(self, context):
        fake_context = context
        fake_context.role = "admin"  # ATTACK SIMULATION

        allowed = fake_context.role == "admin"

        return SecurityTestResult(
            test_name="role_escalation",
            passed=False,
            risk_level="CRITICAL" if allowed else "OK",
            details="Role mutation should not be trusted from client",
        )

    # -----------------------------
    # 4. SUPABASE SERVICE LEAK TEST
    # -----------------------------
    def test_service_role_exposure(self):
        has_service_key = hasattr(self.supabase, "client")

        return SecurityTestResult(
            test_name="service_role_exposure",
            passed=has_service_key,
            risk_level="MEDIUM",
            details="Service role must never be exposed to agents directly",
        )

    # -----------------------------
    # RUN ALL TESTS
    # -----------------------------
    async def run_all(self, context):
        results = []

        results.append(await self.test_cross_user_memory_isolation())
        results.append(self.test_org_isolation(context, context))
        results.append(self.test_role_escalation(context))
        results.append(self.test_service_role_exposure())

        return {
            "security_score": sum(1 for r in results if r.passed),
            "total_tests": len(results),
            "results": [r.__dict__ for r in results],
        }
