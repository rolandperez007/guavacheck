from app.core.austin_brain_v2 import AustinBrainV2


class ToolRouter:
    """
    v2 router = AI decision layer (Austin Brain)
    """

    def __init__(self, tools=None):
        self.tools = tools or {}
        self.brain = AustinBrainV2()

    def route(self, query: str):
        decision = self.brain.route(query)

        return decision["tool"]

    def route_full(self, query: str):
        return self.brain.route(query)