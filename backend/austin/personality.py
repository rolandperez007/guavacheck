"""
Austin Personality

Austin's behaviour is defined by platform doctrine—not hardcoded prompts.

This module loads and exposes the principles that govern every
conversation Austin has with users.

Austin should evolve by updating documentation rather than
rewriting AI logic.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]

DOCS = ROOT / "docs"


@dataclass
class PersonalityDocument:

    name: str

    path: Path

    required: bool = True

    content: str = ""


class AustinPersonality:

    def __init__(self):

        self.documents = [

            PersonalityDocument(
                "Austin",
                DOCS / "AUSTIN.md",
            ),

            PersonalityDocument(
                "Doctrine",
                DOCS / "GUAVA_DOCTRINE.md",
            ),

            PersonalityDocument(
                "UI Bible",
                DOCS / "UI_BIBLE.md",
            ),

            PersonalityDocument(
                "Vision",
                DOCS / "VISION.md",
                required=False,
            ),

            PersonalityDocument(
                "Ecosystem",
                DOCS / "ECOSYSTEM.md",
                required=False,
            ),

        ]

    def load(self):

        loaded = 0

        for document in self.documents:

            if document.path.exists():

                document.content = document.path.read_text(
                    encoding="utf-8"
                )

                loaded += 1

            elif document.required:

                raise FileNotFoundError(
                    f"Missing doctrine document: {document.path}"
                )

        return loaded

    def combined(self):

        sections = []

        for document in self.documents:

            if document.content.strip():

                sections.append(

                    f"""
==================================================
{document.name.upper()}
==================================================

{document.content}
"""
                )

        return "\n".join(sections)

    def summary(self):

        return {

            "documents": len(self.documents),

            "loaded": sum(
                1
                for d in self.documents
                if d.content
            ),

            "required": sum(
                1
                for d in self.documents
                if d.required
            ),

        }


personality = AustinPersonality()