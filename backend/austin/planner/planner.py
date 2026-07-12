"""
Austin Planner

Transforms a user request into a structured execution plan.
"""

from __future__ import annotations

from .models import ExecutionPlan, ExecutionTask


class AustinPlanner:
    """
    Generates execution plans for Austin.
    """

    def create_plan(
        self,
        message: str,
        intent: str = "chat",
        engine: str = "austin",
        confidence: float = 0.95,
    ) -> ExecutionPlan:

        tasks = [
            ExecutionTask(
                id=1,
                name="analyze_request",
                description="Analyze the user's request.",
            ),
            ExecutionTask(
                id=2,
                name="build_context",
                description="Build conversation context.",
            ),
            ExecutionTask(
                id=3,
                name="select_engine",
                description="Determine the best engine.",
            ),
            ExecutionTask(
                id=4,
                name="execute",
                description="Execute the selected engine.",
            ),
            ExecutionTask(
                id=5,
                name="store_memory",
                description="Persist conversation memory.",
            ),
            ExecutionTask(
                id=6,
                name="publish_events",
                description="Publish lifecycle events.",
            ),
        ]

        return ExecutionPlan(
            intent=intent,
            confidence=confidence,
            engine=engine,
            tasks=tasks,
            metadata={
                "message": message,
            },
        )


planner = AustinPlanner()
