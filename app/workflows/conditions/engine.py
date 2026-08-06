from .registry import ConditionRegistry


class ConditionEngine:
    """
    Evaluates workflow conditions.
    """

    def __init__(self):
        self.registry = ConditionRegistry()

    def evaluate(
        self,
        name: str,
        context,
    ) -> bool:

        condition = self.registry.resolve(
            name,
        )

        return condition.evaluate(
            context,
        )