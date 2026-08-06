from __future__ import annotations


class WorkflowRegistry:
    """
    Runtime registry for workflows.
    """

    def __init__(self) -> None:
        self._workflows: dict[str, object] = {}

    def register(
        self,
        name: str,
        workflow: object,
    ) -> None:
        self._workflows[name] = workflow

    def resolve(
        self,
        name: str,
    ):
        return self._workflows[name]