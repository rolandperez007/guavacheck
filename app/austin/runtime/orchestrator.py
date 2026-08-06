"""
Austin Cognitive Orchestrator

Coordinates intent understanding,
context management,
and reasoning.
"""


from app.austin.runtime.intent import IntentNormalizer

from app.austin.runtime.context import SessionContext

from app.austin.runtime.reasoning import ReasoningPlanner



class AustinOrchestrator:


    def __init__(
        self,
        context=None,
    ):


        self.normalizer = IntentNormalizer()


        self.context = context or SessionContext()


        self.planner = ReasoningPlanner()



    def process(
        self,
        message,
    ):


        intent_result = self.normalizer.detect_intent(
            message
        )


        plan = self.planner.plan(

            intent_result["intent"],

            self.context.snapshot(),

        )


        self.context.remember_action(

            plan["action"]

        )


        return {

            "input": message,

            "intent": intent_result,

            "plan": plan,

            "context": self.context.snapshot(),

        }