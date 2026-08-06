from __future__ import annotations

from app.institution.adapters.base import BaseWorkflowAdapter, WorkflowExecutionContext, WorkflowResult


class CurrencyAdapter(BaseWorkflowAdapter):
    """
    Adapter for the Currency module.
    """

    def normalize(
        self,
        context: WorkflowExecutionContext,
        code: str,
    ) -> WorkflowResult:
        normalized = code.upper()
        return self.build_result(
            "currency.normalized",
            data={
                "workflow_id": context.workflow_id,
                "execution_id": context.execution_id,
                "currency": normalized,
                "iso_code": normalized,
            },
        )
