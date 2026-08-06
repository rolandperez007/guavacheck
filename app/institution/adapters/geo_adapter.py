from __future__ import annotations

from app.institution.adapters.base import BaseWorkflowAdapter, WorkflowExecutionContext, WorkflowResult


class GeoAdapter(BaseWorkflowAdapter):
    """
    Adapter for the Geo module.
    """

    def resolve(
        self,
        context: WorkflowExecutionContext,
        address: str,
    ) -> WorkflowResult:
        return self.build_result(
            "geo.resolved",
            data={
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "address": address,
                "location": {"country": "NG", "city": "Lagos"},
            },
        )
