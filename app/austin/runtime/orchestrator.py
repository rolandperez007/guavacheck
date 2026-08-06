"""
Austin Cognitive Orchestrator

Coordinates the complete Austin
runtime execution pipeline.
"""

from app.austin.runtime.intent import IntentNormalizer
from app.austin.runtime.context import SessionContext
from app.austin.runtime.reasoning import ReasoningPlanner
from app.austin.runtime.world import WorldResolver
from app.austin.runtime.router import EngineRouter
from app.austin.runtime.execution import EngineExecutor


class AustinOrchestrator:

    def __init__(
        self,
        registry=None,
        context=None,
        graph=None,
    ):

        self.context = context or SessionContext()

        self.intent = IntentNormalizer()

        self.world = WorldResolver(
            registry=registry,
            graph=graph,
        )

        self.router = EngineRouter(
            registry,
        )

        self.executor = EngineExecutor()

        self.reasoning = ReasoningPlanner()

    def process(
        self,
        message,
        location=None,
    ):

        intent = self.intent.detect_intent(
            message
        )

        world = None

        if location:
            world = self.world.resolve(
                location
            )

        plan = self.reasoning.plan(

            intent["intent"],

            {
                **self.context.snapshot(),
                "world": world,
            },
        )

        engine = self.router.route(
            intent["intent"]
        )

        execution = self.executor.execute(

            engine,

            message,

        )

        self.context.remember_action(
            plan["action"]
        )

        return {

            "status": "success",

            "intent": intent,

            "world": world,

            "plan": plan,

            "execution": execution,

            "context": self.context.snapshot(),

        }