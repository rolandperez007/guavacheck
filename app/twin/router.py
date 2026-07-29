from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

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