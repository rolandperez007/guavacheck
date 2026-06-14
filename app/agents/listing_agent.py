from app.services.database.supabase_service import SupabaseGateway


class ListingAgent:
    def __init__(self):
        self.db = SupabaseGateway()

    async def run(self, query: str, context=None):
        """
        Austin Listing Agent

        Handles:
        - property search
        - location search
        - listing retrieval
        """

        try:
            location = None

            if query:
                query_lower = query.lower()

                trigger_words = [
                    "in ",
                    "at ",
                    "around ",
                    "near ",
                    "lekki",
                    "ajah",
                    "ikoyi",
                    "vi",
                    "victoria island",
                    "chevron",
                    "sangotedo",
                    "ikate",
                    "agungi",
                    "osapa",
                ]

                for word in trigger_words:
                    if word in query_lower:
                        location = query
                        break

            properties = self.db.search_properties(location=location, context=context)

            if properties is None:
                properties = []

            return {
                "success": True,
                "agent": "listing",
                "count": len(properties),
                "results": properties,
            }

        except Exception as e:
            return {
                "success": False,
                "agent": "listing",
                "error": str(e),
                "results": [],
            }
