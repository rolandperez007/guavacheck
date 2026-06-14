from fastapi import APIRouter

from app.services.ai_ratings import get_system_snapshot
from irongate.ai.metrics import get_user_metrics
from irongate.ai.redis_client import client

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def dashboard_summary():
    return get_system_snapshot()


@router.get("/user/{user_id}")
def get_user(user_id: str):
    return get_user_metrics(user_id)


@router.get("/users")
def list_users():
    keys = client.keys("irongate:rep:*")

    users = []
    for key in keys[:50]:
        user_id = key.replace("irongate:rep:", "")
        users.append(get_user_metrics(user_id))

    return {"total_users": len(users), "users": users}
