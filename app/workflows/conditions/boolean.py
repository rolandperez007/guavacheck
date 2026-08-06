from .base import BaseCondition


class BooleanCondition(BaseCondition):

    name = "boolean"

    def evaluate(
        self,
        context,
    ) -> bool:

        return bool(context)