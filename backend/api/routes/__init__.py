"""
guavacheck API Routes

Central route registry.
"""

from .health import router as health_router
from .austin import router as austin_router

__all__ = [

    "health_router",

    "austin_router",

]