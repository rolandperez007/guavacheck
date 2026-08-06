from __future__ import annotations


class WorkflowRegistry:
    """
    Registry of workflow templates,
    actions and triggers.
    """

    def __init__(self) -> None:
        self.actions: dict[str, object] = {}
        self.triggers: dict[str, object] = {}
        self.templates: dict[str, object] = {}

    def register_action(
        self,
        name: str,
        action: object,
    ) -> None:
        self.actions[name] = action

    def register_trigger(
        self,
        name: str,
        trigger: object,
    ) -> None:
        self.triggers[name] = trigger

    def register_template(
        self,
        name: str,
        template: object,
    ) -> None:
        self.templates[name] = template