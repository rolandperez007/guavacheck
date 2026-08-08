from sqlalchemy.orm import Session

from app.permissions.models.permission import Permission
from app.permissions.schemas.permission import PermissionCreate


class PermissionService:


    def create_permission(
        self,
        db: Session,
        data: PermissionCreate
    ):

        permission = Permission(
            name=data.name,
            resource=data.resource,
            action=data.action
        )


        db.add(permission)

        db.commit()

        db.refresh(permission)


        return permission



    def check_permission(
        self,
        permission: str
    ):

        return permission is not None