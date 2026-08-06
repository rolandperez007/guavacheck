"""
Upload Models
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class UploadedDocument:
    document_id: str

    filename: str

    content_type: str

    file_size: int

    property_id: str | None = None

    uploaded_by: str | None = None

    storage_path: str | None = None

    checksum: str | None = None

    uploaded_at: datetime = field(default_factory=datetime.utcnow)

    status: str = "UPLOADED"
