from app.services.database.supabase_service import SupabaseGateway


class PropertyTools:
    def __init__(self):
        self.db = SupabaseGateway()

    def search_properties(self, location=None, limit=20):
        pass


def search_properties(self, location=None):
    try:
        query = self.db.client.table("properties").select("*")

        if location:
            query = query.ilike("location", f"%{location}%")

        response = query.execute()

        return response.data or []

    except Exception as e:
        print(f"[Austin DB ERROR] {e}")
        return []

    def get_property_by_id(self, property_id: str):
        result = (
            self.db.client.table("properties")
            .select("*")
            .eq("id", property_id)
            .single()
            .execute()
        )

        return result.data
