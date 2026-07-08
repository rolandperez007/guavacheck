"""
guavacheck Verification Engine

Core data models used by
property verification workflows.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Optional



@dataclass
class PropertyIdentity:

    property_id: str

    address: str

    owner_name: Optional[str] = None

    coordinates: Optional[Dict] = None

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )



@dataclass
class VerificationDocument:

    document_id: str

    document_type: str

    filename: str

    extracted_data: Dict = field(
        default_factory=dict
    )

    authenticity_score: float = 0



@dataclass
class VerificationResult:

    property_id: str

    document_score: float = 0

    ownership_score: float = 0

    geospatial_score: float = 0

    fraud_score: float = 0

    final_score: float = 0

    warnings: List[str] = field(
        default_factory=list
    )

    status: str = "PENDING"


    def add_warning(self, message):

        self.warnings.append(message)



@dataclass
class OwnershipRecord:

    owner_name: str

    transaction_date: Optional[str]

    source: str

    confidence: float