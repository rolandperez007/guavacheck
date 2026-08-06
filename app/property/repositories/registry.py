"""
Repository Registry

Provides a single place where the Property Graph
obtains repositories from other domains.

This avoids circular imports throughout the system.
"""

from app.property.repositories.property import PropertyRepository

# Uncomment these as the modules are standardized.
#
# from app.passport.repositories.repository import PassportRepository
# from app.twin.repositories.repository import TwinRepository
# from app.vision.repositories.repository import VisionRepository
# from app.property.repositories.knowledge_repository import PropertyKnowledgeRepository


class RepositoryRegistry:
    def __init__(self):

        self.property = PropertyRepository()

        # self.passport = PassportRepository()
        # self.twin = TwinRepository()
        # self.vision = VisionRepository()
        # self.knowledge = PropertyKnowledgeRepository()
