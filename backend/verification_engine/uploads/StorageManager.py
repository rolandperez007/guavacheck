"""
guavacheck Storage Manager

Initial local storage implementation.

Future:
- Supabase Storage
- AWS S3
- Azure Blob
- Google Cloud Storage
"""

from pathlib import Path
import shutil


class StorageManager:

    def __init__(self):

        self.storage_root = Path("storage")

        self.storage_root.mkdir(
            exist_ok=True
        )


    def save_file(
        self,
        source_file,
        destination_name
    ):

        destination = (
            self.storage_root /
            destination_name
        )


        shutil.copy2(
            source_file,
            destination
        )


        return str(destination)


    def exists(
        self,
        filename
    ):

        return (
            self.storage_root /
            filename
        ).exists()