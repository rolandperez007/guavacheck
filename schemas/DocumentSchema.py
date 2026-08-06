from pydantic import BaseModel


class DocumentUpload(BaseModel):
    property_id: str

    document_type: str

    file_name: str


class DocumentResponse(DocumentUpload):
    id: str

    storage_path: str

    class Config:
        from_attributes = True
