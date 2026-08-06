"""
Verification Certificate Generator
"""

from datetime import datetime
from uuid import uuid4


class CertificateGenerator:
    async def generate(
        self,
        property_id: str,
        trust_score: int,
    ):

        return {
            "certificate_id": str(uuid4()),
            "property_id": property_id,
            "trust_score": trust_score,
            "issued_at": datetime.utcnow().isoformat(),
            "issuer": "guavacheck Verification Engine",
            "status": ("VERIFIED" if trust_score >= 70 else "FAILED"),
        }
