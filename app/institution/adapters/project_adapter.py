from __future__ import annotations

from app.institution.adapters.base import BaseWorkflowAdapter, WorkflowExecutionContext, WorkflowResult


class ProjectAdapter(BaseWorkflowAdapter):
    """
    Adapter for the Projects module.
    """

    def create(
        self,
        context: WorkflowExecutionContext,
        payload: dict,
    ) -> WorkflowResult:
        return self.build_result(
            "project.created",
            data={
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "project": payload,
            },
        )
