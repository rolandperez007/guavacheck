class BaseAgent:
    def __init__(self, services):
        self.services = services

    async def run(self, query: str):
        raise NotImplementedError
        class ListingAgent(BaseAgent):

    async def run(self, query: str):

        location = None
        if "lekki" in query.lower():
            location = "Lekki"

        properties = self.services["supabase"].search_properties(location)

        return {
            "message": "Live properties retrieved",
            "count": len(properties),
            "results": properties
        }
