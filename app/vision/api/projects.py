from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.db.dependencies import get_db

from app.vision.models.project import VisionProject
from app.vision.schemas.project import (
    VisionProjectCreate,
    VisionProjectUpdate,
    VisionProjectResponse,
)
from app.vision.services.vision_service import VisionService

router = APIRouter(
    prefix="/projects",
    tags=["Vision Projects"],
)


@router.post(
    "",
    response_model=VisionProjectResponse,
    status_code=201,
)
def create_project(
    payload: VisionProjectCreate,
    db: Session = Depends(get_db),
):

    service = VisionService(db)

    project = VisionProject(
        **payload.model_dump(),
    )

    return service.create_project(project)


@router.get(
    "",
    response_model=list[VisionProjectResponse],
)
def list_projects(
    db: Session = Depends(get_db),
):

    service = VisionService(db)

    return service.list_projects()


@router.get(
    "/{project_id}",
    response_model=VisionProjectResponse,
)
def get_project(
    project_id: str,
    db: Session = Depends(get_db),
):

    service = VisionService(db)

    project = service.get_project(project_id)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    return project


@router.put(
    "/{project_id}",
    response_model=VisionProjectResponse,
)
def update_project(
    project_id: str,
    payload: VisionProjectUpdate,
    db: Session = Depends(get_db),
):

    service = VisionService(db)

    project = service.get_project(project_id)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    for key, value in payload.model_dump(
        exclude_unset=True,
    ).items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)

    return project


@router.delete(
    "/{project_id}",
    status_code=204,
)
def delete_project(
    project_id: str,
    db: Session = Depends(get_db),
):

    service = VisionService(db)

    project = service.get_project(project_id)

    if project is None:
        raise HTTPException(
            status_code=404,
            detail="Project not found",
        )

    db.delete(project)
    db.commit()