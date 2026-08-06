"""
Engineering Models

Shared engineering data models.
"""

from dataclasses import dataclass


@dataclass
class StructuralMember:
    name: str

    length: float

    width: float

    height: float

    material: str
