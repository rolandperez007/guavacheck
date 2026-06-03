import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(dotenv_path=".env")

class SupabaseService:

    from supabase import create_client
import os


class SupabaseService:

    def __init__(self):

        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

        if not url or not key:
            raise Exception("Missing SUPABASE_URL or SERVICE_ROLE_KEY")

        self.client = create_client(url, key)
        

    def search_properties(self, location=None):

        query = (
            self.client
            .table("properties")
            .select("*")
        )

        if location:
            query = query.ilike(
                "location",
                f"%{location}%"
            )

        result = query.execute()

        return result.data