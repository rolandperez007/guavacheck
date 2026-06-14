# app/core/jobs/job_store.py


class JobStore:
    def __init__(self, supabase):
        self.db = supabase

    def create_job(self, job: dict):
        return self.db.table("jobs").insert(job).execute()

    def get_job(self, job_id: str):
        return self.db.table("jobs").select("*").eq("job_id", job_id).single().execute()

    def update_job(self, job_id: str, updates: dict):
        return self.db.table("jobs").update(updates).eq("job_id", job_id).execute()
