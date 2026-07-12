"""
Austin Planner Models

Defines the execution plan generated before Austin
dispatches work to an engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class ExecutionTask:
    """
    A single unit of work in an execution plan.
    """

    id: int
    name: str
    description: str
    completed: bool = False
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ExecutionPlan:
    """
    Complete execution plan produced by Austin.
    """

    intent: str
    confidence: float
    engine: str
    tasks: list[ExecutionTask] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def total_tasks(self) -> int:
        return len(self.tasks)

    @property
    def completed_tasks(self) -> int:
        return sum(task.completed for task in self.tasks)

    @property
    def progress(self) -> float:
        if not self.tasks:
            return 0.0
        return self.completed_tasks / self.total_tasks