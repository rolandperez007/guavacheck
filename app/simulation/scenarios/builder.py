from app.simulation.scenarios.base import BaseScenario


class ScenarioBuilder:
    """
    Fluent builder for simulation scenarios.
    """

    def create(
        self,
        scenario: BaseScenario,
    ) -> BaseScenario:
        return scenario.clone()