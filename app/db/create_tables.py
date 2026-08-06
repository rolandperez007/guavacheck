from app.db.base import Base
from app.db.session import engine

# Core
import app.passport.models.passport  # noqa: F401
import app.twin.models  # noqa: F401

# Vision
import app.vision.models  # noqa: F401

# Institution
import app.institution.models  # noqa: F401

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")