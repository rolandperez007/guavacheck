"""
Austin Context Engine
"""

from .builder import context_builder

# Compatibility alias for legacy imports
context_manager = context_builder

__all__ = [
    "context_builder",
    "context_manager",
]