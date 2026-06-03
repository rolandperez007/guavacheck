class ListingMemory:

    def __init__(self, supabase):
        self.db = supabase

    def store_search(self, query, results):
        self.db.client.table("search_history").insert({
            "query": query,
            "result_count": len(results)
        }).execute()

    def recent_context(self):
        return self.db.client.table("search_history")\
            .select("*")\
            .order("created_at", desc=True)\
            .limit(5)\
            .execute().data