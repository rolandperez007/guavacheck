"""
Property Engine

Responsible for property search,
recommendations and discovery.
"""

from backend.engines.base import BaseEngine

from .search import property_search


class PropertyEngine(BaseEngine):

    name = "property"

    version = "1.0.0"

    description = "Property Discovery Engine"

    async def execute(self, request: dict):
        self.kernel.log(
            message="property engine executed",
            correlation_id=request.get("correlation_id"),
            trace_id=request.get("trace_id"),
            engine=self.name,
            service="engines.property",
        )
        action = request.get(

            "action",

            "search",

        )

        if action == "search":

            return property_search.search(request)

        return {

            "engine": self.name,

            "status": "completed",

            "message": "No matching action.",

        }