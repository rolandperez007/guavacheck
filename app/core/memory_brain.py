from datetime import datetime
from app.services.supabase_service import SupabaseService


class MemoryBrain:
    """
    Persistent memory system (Supabase-backed)
    """

    def __init__(self):
        self.db = SupabaseService()

    def remember_query(self, user_id: str, query: str):
        try:
            data = {
                "user_id": user_id,
                "key": "query",
                "value": {
                    "text": query,
                    "timestamp": str(datetime.utcnow())
                }
            }

            self.db.client.table("user_memory").insert(data).execute()

        except Exception as e:
            print("Memory write error:", str(e))

    def infer_preferences(self, user_id: str):
        try:
            res = (
                self.db.client
                .table("user_memory")
                .select("*")
                .eq("user_id", user_id)
                .execute()
            )

            rows = res.data or []

            locations = []
            keywords = []

            for r in rows:
                val = r.get("value", {})
                text = (val.get("text") or "").lower()

                if "lekki" in text:
                    locations.append("Lekki")
                if "apartment" in text or "house" in text:
                    keywords.append(text)

            return {
                "locations": list(set(locations)),
                "keywords": keywords[-10:]
            }

        except Exception as e:
            print("Memory read error:", str(e))
            return {"locations": [], "keywords": []}