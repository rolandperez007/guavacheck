from app.services.supabase_service import SupabaseService

class ListingSwarmAgent:
    def __init__(self):
        self.db = SupabaseService()

    def run(self, location=None):
        return self.db.search_properties(location) or []