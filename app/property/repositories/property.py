from sqlalchemy.orm import Session

from app.property.models.property import Property
from app.property.schemas.property import PropertyCreate


class PropertyRepository:


    def create(
        self,
        db: Session,
        data: PropertyCreate
    ) -> Property:

        property = Property(
            **data.model_dump()
        )

        db.add(property)

        db.commit()

        db.refresh(property)

        return property



    def get_by_id(
        self,
        db: Session,
        property_id: str
    ) -> Property | None:

        return (
            db.query(Property)
            .filter(
                Property.id == property_id
            )
            .first()
        )



    def get_by_reference(
        self,
        db: Session,
        reference_code: str
    ) -> Property | None:

        return (
            db.query(Property)
            .filter(
                Property.reference_code == reference_code
            )
            .first()
        )