"""
Austin Engine Router

Selects the correct engine
for a given intent.
"""


class EngineRouter:

    def __init__(
        self,
        registry,
    ):
        self.registry = registry

        self.routes = {
            "load": "property",
            "create": "property",
            "property_search": "property",
            "construction_estimate": "construction",
            "verify_property": "verification",
            "mortgage": "mortgage",
        }

    def route(
        self,
        intent,
    ):

        engine_name = self.routes.get(intent)

        if not engine_name:
            return None

        return self.registry.get(
            engine_name
        )