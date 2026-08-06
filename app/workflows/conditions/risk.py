from .base import BaseCondition


class RiskCondition(BaseCondition):

    name = "risk"

    def evaluate(
        self,
        context,
    ) -> bool:

        return True