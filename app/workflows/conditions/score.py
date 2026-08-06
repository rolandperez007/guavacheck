from .base import BaseCondition


class ScoreCondition(BaseCondition):

    name = "score"

    def evaluate(
        self,
        context,
    ) -> bool:

        return True