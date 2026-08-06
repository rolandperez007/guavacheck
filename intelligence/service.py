class IntelligenceService:
    async def store(self, event):

        # TODO
        # Save into Supabase

        return {
            "status": "stored",
            "event": event.event_name,
        }


service = IntelligenceService()
