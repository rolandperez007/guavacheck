"""
Property Engine

Responsible for property search,
recommendations and discovery.
"""

from engines.base import BaseEngine

from .search import property_search


class PropertyEngine(BaseEngine):

    name = "property"

    version = "1.0.0"

    description = "Property Discovery Engine"

    async def execute(self, request: dict):

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