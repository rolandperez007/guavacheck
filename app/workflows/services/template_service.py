class TemplateService:
    """
    Workflow template management.
    """

    def __init__(self):
        self.templates = {}

    def register(
        self,
        name: str,
        template,
    ):
        self.templates[name] = template

    def get(
        self,
        name: str,
    ):
        return self.templates.get(name)

    def list(self):
        return sorted(self.templates.keys())