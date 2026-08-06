from .repository import InstitutionWorkflowRepository


class InstitutionWorkflowService:
    """
    Business service for institution workflows.
    """

    def __init__(
        self,
        repository: InstitutionWorkflowRepository,
    ):
        self.repository = repository

    def list_workflows(
        self,
        institution_id,
    ):
        return self.repository.workflows(
            institution_id,
        )

    def create(
        self,
        workflow,
    ):
        return self.repository.save(
            workflow,
        )