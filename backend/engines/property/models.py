"""
Property Models
"""

from dataclasses import dataclass
from typing import Optional


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

    land_size: Optional[float] = None

    available: bool = True