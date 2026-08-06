"""
Austin Reasoning Planner

Creates structured execution plans
from intent and context.
"""


class ReasoningPlanner:


    def __init__(
        self,
    ):

        self.actions = {

            "load": "load_world_context",

            "create": "create_resource",

            "property": "analyse_property",

        }



    def plan(
        self,
        intent,
        context=None,
    ):


        action = self.actions.get(

            intent,

            "unknown_action",

        )


        return {

            "intent": intent,

            "action": action,

            "context": context or {},

        }