from __future__ import annotations

from .base import BaseWorkflowTrigger


class WorkflowTriggerRegistry:
    """
    Runtime registry of workflow triggers.
    """

    def __init__(self):
        self._triggers: dict[
            str,
            BaseWorkflowTrigger,
        ] = {}

    def register(
        self,
        trigger: BaseWorkflowTrigger,
    ):
        self._triggers[trigger.name] = trigger

    def resolve(
        self,
        name: str,
    ):
        return self._triggers[name]

    def list(self):
        return sorted(self._triggers.keys())