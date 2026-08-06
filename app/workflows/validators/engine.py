from .registry import ValidationRegistry


class ValidationEngine:
    """
    Runs all registered validators.
    """

    def __init__(self):
        self.registry = ValidationRegistry()

    def validate(
        self,
        workflow,
    ) -> list[str]:

        errors = []

        for validator in self.registry.validators():
            errors.extend(
                validator.validate(
                    workflow,
                )
            )

        return errors