from .repository import SimulationWorkflowRepository


class SimulationWorkflowService:
    """
    Coordinates simulation services.
    """

    def __init__(
        self,
        repository: SimulationWorkflowRepository,
    ):
        self.repository = repository

    def simulations(
        self,
        reference_id,
    ):
        return self.repository.list_by_reference(
            reference_id,
        )