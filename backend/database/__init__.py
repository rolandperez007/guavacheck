"""Database package compatibility layer."""

from __future__ import annotations

from .connection import get_connection
from .models import Base

__all__ = ["Base", "get_connection"]
