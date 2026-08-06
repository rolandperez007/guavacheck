from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.twin.schemas import TwinCreate
from app.twin.service import TwinService

router = APIRouter(
    prefix="/twins",
    tags=["Twin Studio (3D)"],
)


@router.post("/")
def create_twin(
    request: TwinCreate,
    db: Session = Depends(get_db),
):
    return TwinService.create(
        db,
        request,
    )
