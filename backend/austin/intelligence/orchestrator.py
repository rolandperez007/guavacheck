"""
Austin Orchestrator

Coordinates execution across engines.
"""

from __future__ import annotations

from .planner import planner
from .reasoner import reasoner


class AustinOrchestrator:

    def execute(

        self,

        query: str,

    ):

        plan = planner.build(query)

        outputs = {}

        for task in plan.tasks:

            outputs[task.engine] = {

                "status": "completed",

                "task": task.name,

            }

        return reasoner.reason(

            plan,

            outputs,

        )


orchestrator = AustinOrchestrator()