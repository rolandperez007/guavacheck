"""
Austin Cognitive Orchestrator

Coordinates:
- intent understanding
- context management
- world resolution
- reasoning
"""

from app.austin.runtime.intent import IntentNormalizer
from app.austin.runtime.context import SessionContext
from app.austin.runtime.reasoning import ReasoningPlanner
from app.austin.runtime.world import WorldResolver


class AustinOrchestrator:

    def __init__(
        self,
        context=None,
        registry=None,
        graph=None,
    ):
        self.normalizer = IntentNormalizer()
        self.context = context or SessionContext()
        self.world = WorldResolver(
            registry=registry,
            graph=graph,
        )
        self.planner = ReasoningPlanner()

    def process(
        self,
        message,
        location=None,
    ):
        intent_result = self.normalizer.detect_intent(message)

        world_result = None

        if location:
            world_result = self.world.resolve(location)

        plan = self.planner.plan(
            intent_result["intent"],
            {
                **self.context.snapshot(),
                "world": world_result,
            },
        )

        self.context.remember_action(
            plan["action"]
        )

        return {
            "input": message,
            "intent": intent_result,
            "world": world_result,
            "plan": plan,
            "context": self.context.snapshot(),
        }