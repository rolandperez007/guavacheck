"""
guavacheck API Routes

Central route registry.
"""

from .austin import router as austin_router
from .health import router as health_router

__all__ = [
    "austin_router",
    "health_router",
]
