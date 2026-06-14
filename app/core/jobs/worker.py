# app/core/jobs/worker.py

from app.core.jobs.job_store import JobStore


def process_job(job_id: str, job_type: str, payload: dict):
    store = JobStore()

    store.update_job(job_id, {"status": "processing", "progress": 10})

    try:
        if job_type == "pdf_export":
            result = generate_pdf(payload)

        elif job_type == "boq":
            result = generate_boq(payload)

        elif job_type == "mortgage":
            result = run_mortgage(payload)

        else:
            raise Exception("Unknown job type")

        store.update_job(
            job_id, {"status": "completed", "progress": 100, "result": result}
        )

    except Exception as e:
        store.update_job(job_id, {"status": "failed", "error": str(e)})
