"""
Location Node

Represents a location inside Austin's world geography graph.
"""


from dataclasses import dataclass, field



@dataclass
class LocationNode:


    name: str

    level: str

    parent: str | None = None

    children: list = field(
        default_factory=list
    )

    data: dict = field(
        default_factory=dict
    )