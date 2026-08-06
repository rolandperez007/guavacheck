from app.workflows.schemas import WorkflowApproval


class ApprovalBuilder:
    """
    Creates approval requirements.
    """

    def create(
        self,
        role: str,
        timeout_hours: int = 24,
    ):
        return WorkflowApproval(
            role=role,
            timeout_hours=timeout_hours,
        )