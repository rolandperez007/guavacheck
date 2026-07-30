from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.property.schemas.property import (
    PropertyCreate,
    PropertyResponse
)

from app.property.services.property import PropertyService


router = APIRouter(
    prefix="/properties",
    tags=["Properties"]
)


service = PropertyService()



@router.post(
    "",
    response_model=PropertyResponse
)
def create_property(
    payload: PropertyCreate,
    db: Session = Depends(get_db)
):

    return service.create_property(
        db,
        payload
    )



@router.get(
    "/{property_id}",
    response_model=PropertyResponse
)
def get_property(
    property_id: str,
    db: Session = Depends(get_db)
):

    return service.get_property(
        db,
        property_id
    )