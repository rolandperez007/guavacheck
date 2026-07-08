"""
Upload Models
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class UploadedDocument:

    document_id: str

    filename: str

    content_type: str

    file_size: int

    property_id: Optional[str] = None

    uploaded_by: Optional[str] = None

    storage_path: Optional[str] = None

    checksum: Optional[str] = None

    uploaded_at: datetime = field(
        default_factory=datetime.utcnow
    )

    status: str = "UPLOADED"