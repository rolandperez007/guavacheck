from dataclasses import dataclass


@dataclass(frozen=True)
class AIAttribution:
    provider: str = "OpenAI"
    attribution: str = "AI generated with OpenAI"
    disclosure: str = (
        "This content was generated with the assistance of OpenAI technology."
    )


OPENAI_ATTRIBUTION = AIAttribution()


def get_openai_attribution() -> dict[str, str]:
    return {
        "provider": OPENAI_ATTRIBUTION.provider,
        "attribution": OPENAI_ATTRIBUTION.attribution,
        "disclosure": OPENAI_ATTRIBUTION.disclosure,
    }


def apply_openai_attribution(
    content: str,
    include_disclosure: bool = False,
) -> str:
    if not content:
        return content

    if include_disclosure:
        return (
            f"{content}\n\n"
            f"— {OPENAI_ATTRIBUTION.attribution}"
        )

    return content