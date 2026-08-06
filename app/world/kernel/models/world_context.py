from dataclasses import dataclass


@dataclass
class WorldContext:

    country: str

    district: str | None = None

    sector: str | None = None

    requirements: dict | None = None