from __future__ import annotations

from .base import BaseWorkflowAction


class WorkflowActionRegistry:
    """
    Registry of executable workflow actions.
    """

    def __init__(self):
        self._actions: dict[
            str,
            BaseWorkflowAction,
        ] = {}

    def register(
        self,
        action: BaseWorkflowAction,
    ):
        self._actions[action.name] = action

    def resolve(
        self,
        name: str,
    ):
        return self._actions[name]

    def list(self):
        return sorted(
            self._actions.keys(),
        )