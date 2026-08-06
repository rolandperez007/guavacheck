from .base import BaseWorkflowValidator


class ValidationRegistry:
    """
    Registry of workflow validators.
    """

    def __init__(self):
        self._validators: list[
            BaseWorkflowValidator
        ] = []

    def register(
        self,
        validator: BaseWorkflowValidator,
    ):
        self._validators.append(
            validator,
        )

    def validators(self):
        return self._validators