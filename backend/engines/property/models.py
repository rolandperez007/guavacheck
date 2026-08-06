"""
Property Models
"""

from dataclasses import dataclass


@dataclass
class Property:
    id: str

    title: str

    location: str

    property_type: str

    bedrooms: int

    bathrooms: int

    price: float

    currency: str

    land_size: float | None = None

    available: bool = True
