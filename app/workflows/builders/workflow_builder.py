from __future__ import annotations

from app.workflows.schemas import WorkflowSchema


class WorkflowBuilder:
    """
    Fluent builder for enterprise workflows.
    """

    def __init__(
        self,
        name: str,
    ) -> None:

        self.workflow = WorkflowSchema(
            name=name,
        )

    def description(
        self,
        description: str,
    ):
        self.workflow.description = description
        return self

    def version(
        self,
        version: str,
    ):
        self.workflow.version = version
        return self

    def add_node(
        self,
        node,
    ):
        self.workflow.nodes.append(node)
        return self

    def build(self):
        return self.workflow