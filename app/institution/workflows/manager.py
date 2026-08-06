from .service import InstitutionWorkflowService


class InstitutionWorkflowManager:
    """
    High-level orchestration for institution workflows.
    """

    def __init__(
        self,
        service: InstitutionWorkflowService,
    ):
        self.service = service

    def deploy(
        self,
        workflow,
    ):
        return self.service.create(
            workflow,
        )