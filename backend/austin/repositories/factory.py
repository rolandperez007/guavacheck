"""
Austin Repository Factory

Chooses which repository implementation Austin uses.
"""

from __future__ import annotations

from .memory.event_repository import MemoryEventRepository

#
# Production switch happens here.
#
# Later this will become:
#
# from .database.event_repository import DatabaseEventRepository
# event_repository = DatabaseEventRepository()
#

event_repository = MemoryEventRepository()
