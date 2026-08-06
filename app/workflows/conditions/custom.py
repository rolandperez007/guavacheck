from .base import BaseCondition


class CustomCondition(BaseCondition):
    """
    User-defined condition.
    """

    name = "custom"

    def __init__(
        self,
        evaluator,
    ):
        self.evaluator = evaluator

    def evaluate(
        self,
        context,
    ) -> bool:

        return self.evaluator(
            context,
        )