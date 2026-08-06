from .base import BaseCondition


class ConditionRegistry:
    """
    Runtime registry of conditions.
    """

    def __init__(self):
        self._conditions: dict[
            str,
            BaseCondition,
        ] = {}

    def register(
        self,
        condition: BaseCondition,
    ):
        self._conditions[
            condition.name
        ] = condition

    def resolve(
        self,
        name: str,
    ):
        return self._conditions[name]

    def list(self):
        return sorted(
            self._conditions.keys()
        )