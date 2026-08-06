import base64
import os
from typing import Any

from openai import OpenAI

from app.vision.providers.base import VisionProvider


class OpenAIProvider(VisionProvider):
    """
    OpenAI Vision Provider

    Supports:

    • Interior rendering
    • Exterior rendering
    • Floorplan generation
    • Future image editing
    • Future image variations

    Returns a normalized response so the rest of the
    Vision Engine is provider-independent.
    """

    DEFAULT_MODEL = "gpt-image-1"
    DEFAULT_SIZE = "1536x1536"
    DEFAULT_QUALITY = "high"

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured.")

        self.client = OpenAI(
            api_key=api_key,
        )

    # ---------------------------------------------------------
    # Internal helper
    # ---------------------------------------------------------

    def _generate(
        self,
        prompt: str,
        *,
        size: str | None = None,
        quality: str | None = None,
        model: str | None = None,
    ) -> dict[str, Any]:

        response = self.client.images.generate(
            model=model or self.DEFAULT_MODEL,
            prompt=prompt,
            size=size or self.DEFAULT_SIZE,
            quality=quality or self.DEFAULT_QUALITY,
        )

        image = response.data[0]

        return {
            "provider": "openai",
            "model": model or self.DEFAULT_MODEL,
            "prompt": prompt,
            "image": image,
            "b64_json": getattr(image, "b64_json", None),
            "url": getattr(image, "url", None),
            "revised_prompt": getattr(
                image,
                "revised_prompt",
                None,
            ),
        }

    # ---------------------------------------------------------
    # Interior
    # ---------------------------------------------------------

    def generate_interior(
        self,
        prompt: str,
    ):

        return self._generate(prompt)

    # ---------------------------------------------------------
    # Exterior
    # ---------------------------------------------------------

    def generate_exterior(
        self,
        prompt: str,
    ):

        return self._generate(prompt)

    # ---------------------------------------------------------
    # Floorplan
    # ---------------------------------------------------------

    def generate_floorplan(
        self,
        prompt: str,
    ):

        return self._generate(prompt)

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def save_base64_image(
        self,
        b64_string: str,
        output_path: str,
    ) -> str:
        """
        Saves a Base64 image to disk.

        Returns:
            output path
        """

        image_bytes = base64.b64decode(
            b64_string,
        )

        with open(output_path, "wb") as f:
            f.write(image_bytes)

        return output_path

    # ---------------------------------------------------------
    # Future Feature
    # ---------------------------------------------------------

    def edit_image(
        self,
        image_path: str,
        prompt: str,
    ):
        """
        Reserved for future support.

        GPT Image supports image editing.
        """

        raise NotImplementedError

    # ---------------------------------------------------------
    # Future Feature
    # ---------------------------------------------------------

    def create_variation(
        self,
        image_path: str,
    ):
        """
        Reserved for future image variations.
        """

        raise NotImplementedError
