from .base import BaseWorkflowValidator


class WorkflowValidator(BaseWorkflowValidator):

    name = "workflow"

    def validate(
        self,
        workflow,
    ) -> list[str]:

        errors = []

        if not getattr(workflow, "name", None):
            errors.append(
                "Workflow name is required."
            )

        if not getattr(workflow, "nodes", None):
            errors.append(
                "Workflow contains no nodes."
            )

        return errors