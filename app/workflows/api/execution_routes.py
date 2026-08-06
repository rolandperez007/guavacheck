from fastapi import APIRouter

router = APIRouter(
    prefix="/executions",
)


@router.post("/{workflow_id}/start")
async def start_workflow(
    workflow_id: str,
):
    return {
        "workflow_id": workflow_id,
        "status": "started",
    }


@router.post("/{execution_id}/pause")
async def pause_execution(
    execution_id: str,
):
    return {
        "execution_id": execution_id,
        "status": "paused",
    }


@router.post("/{execution_id}/resume")
async def resume_execution(
    execution_id: str,
):
    return {
        "execution_id": execution_id,
        "status": "running",
    }


@router.post("/{execution_id}/cancel")
async def cancel_execution(
    execution_id: str,
):
    return {
        "execution_id": execution_id,
        "status": "cancelled",
    }