from app.services.database.supabase_service import SupabaseGateway


class ListingSwarmAgent:
    def __init__(self):
        self.db = SupabaseGateway()

    def run(self, location=None):
        return self.db.search_properties(location) or []
