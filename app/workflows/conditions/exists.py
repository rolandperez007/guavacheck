from .base import BaseCondition


class ExistsCondition(BaseCondition):

    name = "exists"

    def evaluate(
        self,
        context,
    ) -> bool:

        return context is not None