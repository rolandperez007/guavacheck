from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def list_workflows():
    """
    List all workflows.
    """
    return {
        "success": True,
        "data": [],
    }


@router.get("/{workflow_id}")
async def get_workflow(
    workflow_id: str,
):
    return {
        "success": True,
        "workflow_id": workflow_id,
    }


@router.post("/")
async def create_workflow():
    return {
        "success": True,
        "message": "Workflow created.",
    }


@router.put("/{workflow_id}")
async def update_workflow(
    workflow_id: str,
):
    return {
        "success": True,
        "workflow_id": workflow_id,
    }


@router.delete("/{workflow_id}")
async def delete_workflow(
    workflow_id: str,
):
    return {
        "success": True,
        "workflow_id": workflow_id,
    }