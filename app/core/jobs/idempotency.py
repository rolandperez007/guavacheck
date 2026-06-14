# app/core/jobs/idempotency.py


class IdempotencyStore:
    def __init__(self, db):
        self.db = db

    def exists(self, key: str):
        return self.db.table("idempotency").select("*").eq("key", key).execute()

    def save(self, key: str, job_id: str):
        return (
            self.db.table("idempotency")
            .insert({"key": key, "job_id": job_id})
            .execute()
        )
