"""
guavacheck Upload Manager

Coordinates document uploads for
the Verification Engine.
"""

import uuid

from .FileValidator import FileValidator
from .StorageManager import StorageManager
from .UploadModels import UploadedDocument


class UploadManager:

    def __init__(self):

        self.validator = FileValidator()

        self.storage = StorageManager()


    def upload(
        self,
        file_path,
        content_type,
        file_size
    ):

        valid, message = self.validator.validate(
            file_path,
            file_size
        )


        if not valid:

            raise ValueError(message)


        document_id = str(
            uuid.uuid4()
        )


        destination = (
            f"{document_id}_"
            f"{file_path.split('/')[-1]}"
        )


        storage_path = self.storage.save_file(
            file_path,
            destination
        )


        return UploadedDocument(

            document_id=document_id,

            filename=file_path,

            content_type=content_type,

            file_size=file_size,

            storage_path=storage_path

        )