from .base import BaseCondition


class RoleCondition(BaseCondition):

    name = "role"

    def evaluate(
        self,
        context,
    ) -> bool:

        return True