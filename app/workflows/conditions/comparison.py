from .base import BaseCondition


class ComparisonCondition(BaseCondition):

    name = "comparison"

    def evaluate(
        self,
        context,
    ) -> bool:

        return True