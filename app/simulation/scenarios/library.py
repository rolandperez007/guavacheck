from app.simulation.scenarios.base import BaseScenario


class ScenarioLibrary:
    """
    Registry of reusable scenario templates.
    """

    def __init__(self) -> None:
        self._scenarios: dict[str, BaseScenario] = {}

    def register(
        self,
        scenario: BaseScenario,
    ) -> None:
        self._scenarios[scenario.name] = scenario

    def get(
        self,
        name: str,
    ) -> BaseScenario:
        return self._scenarios[name]

    def list(self) -> list[str]:
        return sorted(self._scenarios.keys())