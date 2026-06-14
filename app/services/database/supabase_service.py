import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()


class SupabaseGateway:
    def __init__(self, context=None):
        self.context = context

        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

        if not url or not key:
            raise Exception("Missing SUPABASE_URL or SERVICE_ROLE_KEY")

        self.client = create_client(url, key)

    def search_properties(self, location=None, context=None):
        query = self.client.table("properties").select("*")

        active_context = context or self.context

        if active_context and getattr(active_context, "org_id", None):
            query = query.eq("org_id", active_context.org_id)

        if location:
            query = query.ilike("location", f"%{location}%")

        return query.execute().data
