from fastapi import APIRouter

router = APIRouter(
    prefix="/templates",
)


@router.get("/")
async def templates():

    return {
        "templates": [],
    }


@router.get("/{template_name}")
async def template(
    template_name: str,
):

    return {
        "template": template_name,
    }


@router.post("/{template_name}/instantiate")
async def instantiate(
    template_name: str,
):

    return {
        "template": template_name,
        "status": "created",
    }