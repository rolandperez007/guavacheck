from __future__ import annotations

from app.institution.adapters.base import BaseWorkflowAdapter, WorkflowExecutionContext, WorkflowResult


class CommunityAdapter(BaseWorkflowAdapter):
    """
    Adapter for the Community module.
    """

    def moderate(
        self,
        context: WorkflowExecutionContext,
        entity_type: str,
    ) -> WorkflowResult:
        return self.build_result(
            "community.moderation.completed",
            data={
                "entity_type": entity_type,
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "moderation": "approved",
            },
        )
