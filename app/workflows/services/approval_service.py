from app.workflows.repositories import ApprovalRepository


class ApprovalService:
    """
    Human approval workflows.
    """

    def __init__(
        self,
        repository: ApprovalRepository,
    ):
        self.repository = repository

    def pending(self):
        return self.repository.pending()

    def approve(
        self,
        approval,
    ):
        approval.approved = True
        self.repository.commit()
        return approval