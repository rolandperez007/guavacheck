# Model registration file.
#
# Importing models here ensures SQLAlchemy
# knows about all tables before migrations
# or metadata creation.


from app.identity.models.identity import Identity
from app.identity.models.organization import Organization

from app.users.models.user import User

from app.auth.models.token import Token

from app.permissions.models.role import Role
from app.permissions.models.permission import Permission


__all__ = [
    "Identity",
    "Organization",
    "User",
    "Token",
    "Role",
    "Permission",
]