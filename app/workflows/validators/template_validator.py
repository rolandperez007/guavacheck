from .base import BaseWorkflowValidator


class TemplateValidator(BaseWorkflowValidator):

    name = "template"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        return []