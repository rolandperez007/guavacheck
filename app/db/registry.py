
Canonical SQLAlchemy model registry,

Every ORM model that participates in the application's
relational database must ultimately be imported through
this module before metadata creation or migration,

The project uses exactly one declarative Base
    app.db.base.Base

# Identity
from app.identity.models.identity import Identity
from app.identity.models.organization import Organization

# Users
from app.users.models.user import User

# Authentication
from app.auth.models.token import Token

# Permissions
from app.permissions.models.role import Role
from app.permissions.models.permission import Permission

# Core application models
import app.passport.models.passport  # noqa: F401
import app.twin.models  # noqa: F401

# Vision
import app.vision.models  # noqa: F401

# Institution
import app.institution.models  # noqa: F401

# Property
import app.property.models.property  # noqa: F401

# Simulation
import app.simulation.models.simulation  # noqa: F401
import app.simulation.models.scenario  # noqa: F401
import app.simulation.models.execution  # noqa: F401
import app.simulation.models.report  # noqa: F401

# Workflows
import app.workflows.models  # noqa: F401


__all__ = [
    "Identity",
    "Organization",
    "User",
    "Token",
    "Role",
    "Permission",
]
