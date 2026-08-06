"""
QR Code Generator

Future implementation:

- PNG QR Codes

- SVG QR Codes

- Signed Verification URLs

- Blockchain Verification
"""


class QRCodeGenerator:
    async def generate(
        self,
        certificate_id: str,
    ):

        return {
            "certificate_id": certificate_id,
            "verification_url": (f"https://verify.guavacheck.com/{certificate_id}"),
            "status": "NOT_IMPLEMENTED",
        }
