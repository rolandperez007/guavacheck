from app.services.supabase_service import SupabaseService

class PropertyService:

    def __init__(self):
        self.db = SupabaseService()

    def search_properties(self):

        return self.db.get_properties()
        def search_properties(
    self,
    location=None,
    max_price=None
):