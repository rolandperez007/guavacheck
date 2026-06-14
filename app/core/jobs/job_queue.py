# app/core/jobs/job_queue.py

from rq import Queue
from app.core.jobs.redis_client import redis_client

job_queue = Queue("austin_jobs", connection=redis_client)
