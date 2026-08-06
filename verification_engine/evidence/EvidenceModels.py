"""
Evidence Models
"""

from dataclasses import dataclass


@dataclass
class Evidence:
    source: str

    description: str

    confidence: float

    payload: dict
