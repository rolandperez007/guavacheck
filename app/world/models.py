from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict
from typing import List
from typing import Optional


@dataclass
class WorldCountry:

    code: str

    name: str

    continent: str

    region: str

    currency: str

    timezone: str

    locale: str

    reference: bool = False

    capabilities: Dict[str, bool] = field(default_factory=dict)

    districts: List[str] = field(default_factory=list)

    metadata: Dict[str, str] = field(default_factory=dict)


@dataclass
class DistrictContext:

    name: str

    country: WorldCountry

    documents: List[str]

    engines: List[str]

    confidence: float = 1.0


@dataclass
class AustinWorldResponse:

    country: str

    district: Optional[str]

    confidence: float

    sources: List[str]

    summary: str

    recommendations: List[str]