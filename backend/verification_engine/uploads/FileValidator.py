"""
Validates uploaded files.
"""

import os


class FileValidator:
    MAX_FILE_SIZE = 20 * 1024 * 1024

    ALLOWED_EXTENSIONS = {".pdf", ".jpg", ".jpeg", ".png", ".tif", ".tiff"}

    def validate(self, filename, file_size):

        extension = os.path.splitext(filename)[1].lower()

        if extension not in self.ALLOWED_EXTENSIONS:
            return False, "Unsupported file type."

        if file_size > self.MAX_FILE_SIZE:
            return False, "File exceeds size limit."

        return True, "Validation successful."
