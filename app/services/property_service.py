from app.services.database.supabase_service import SupabaseGateway

class PropertyService:

    def __init__(self):
        self.db = SupabaseGateway()

    def search_properties(self):

        return self.db.get_properties()
        def search_properties(
    self,
    location=None,
    max_price=None
):
