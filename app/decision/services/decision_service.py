from app.decision.engines.decision_engine import DecisionEngine
from app.decision.models.context import DecisionContext


class DecisionService:
    def __init__(self):

        self.engine = DecisionEngine()

    def evaluate(
        self,
        context: DecisionContext,
    ):

        return self.engine.evaluate(
            context,
        )
