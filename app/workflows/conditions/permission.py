from .base import BaseCondition


class PermissionCondition(BaseCondition):

    name = "permission"

    def evaluate(
        self,
        context,
    ) -> bool:

        return True