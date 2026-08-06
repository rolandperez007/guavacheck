from .repository import PassportWorkflowRepository


class PassportWorkflowService:
    """
    Business logic for passport workflows.
    """

    def __init__(
        self,
        repository: PassportWorkflowRepository,
    ):
        self.repository = repository

    def workflows(
        self,
        passport_id,
    ):
        return self.repository.list_for_passport(
            passport_id,
        )