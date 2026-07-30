from pathlib import Path
import base64
import uuid


class ImageStorage:

    ROOT = Path("storage/renders")

    @classmethod
    def save_base64(
        cls,
        b64_string: str,
        category: str,
    ) -> str:

        folder = cls.ROOT / category

        folder.mkdir(
            parents=True,
            exist_ok=True,
        )

        filename = f"{uuid.uuid4()}.png"

        filepath = folder / filename

        with open(filepath, "wb") as f:
            f.write(
                base64.b64decode(
                    b64_string,
                )
            )

        return str(filepath)