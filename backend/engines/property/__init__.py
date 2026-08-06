"""
Property Engine

Handles property discovery, indexing,
matching and recommendations.
"""

from .engine import PropertyEngine

property_engine = PropertyEngine()

__all__ = [
    "PropertyEngine",
    "property_engine",
]
