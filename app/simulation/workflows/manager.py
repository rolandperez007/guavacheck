from .service import SimulationWorkflowService


class SimulationWorkflowManager:
    """
    Entry point for workflow-driven simulations.
    """

    def __init__(
        self,
        service: SimulationWorkflowService,
    ):
        self.service = service

    def execute(
        self,
        reference_id,
    ):
        return {
            "reference_id": reference_id,
            "status": "simulation_started",
        }