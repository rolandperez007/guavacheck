class WorkflowTemplateRegistry:
    """
    Registry of reusable workflow templates.
    """

    def __init__(self):
        self._templates = {}

    def register(
        self,
        template,
    ):
        self._templates[
            template.name
        ] = template

    def resolve(
        self,
        name: str,
    ):
        return self._templates[name]

    def list(self):
        return sorted(
            self._templates.keys()
        )