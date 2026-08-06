from .service import PassportWorkflowService


class PassportWorkflowManager:
    """
    Coordinates passport lifecycle workflows.
    """

    def __init__(
        self,
        service: PassportWorkflowService,
    ):
        self.service = service

    def initialize(
        self,
        passport_id,
    ):
        return {
            "passport_id": passport_id,
            "status": "initialized",
        }