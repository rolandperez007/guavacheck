"""
Final Verification Result
"""

from dataclasses import dataclass


@dataclass
class VerificationResult:

    success: bool

    property_id: str

    trust_score: int

    certificate: dict

    evidence: list

    summary: str
