from app.vision.providers.google_provider import GoogleProvider
from app.vision.providers.openai_provider import OpenAIProvider
from app.vision.providers.stability_provider import StabilityProvider


class ProviderFactory:

    @staticmethod
    def get(provider_name: str):

        provider_name = provider_name.lower()

        providers = {

            "openai": OpenAIProvider,

            "google": GoogleProvider,

            "stability": StabilityProvider,

        }

        provider = providers.get(provider_name)

        if provider is None:
            raise ValueError(
                f"Unknown provider: {provider_name}"
            )

        return provider()