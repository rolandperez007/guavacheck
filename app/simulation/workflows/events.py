class SimulationWorkflowEvents:

    def simulation_started(
        self,
        simulation_id,
    ):
        return {
            "event": "simulation.started",
            "simulation_id": simulation_id,
        }

    def simulation_completed(
        self,
        simulation_id,
    ):
        return {
            "event": "simulation.completed",
            "simulation_id": simulation_id,
        }