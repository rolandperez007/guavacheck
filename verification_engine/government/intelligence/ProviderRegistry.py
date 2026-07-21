"""
Provider Registry

Manages government data providers,
source priority, reliability weights,
and supported verification capabilities.
"""

from typing import Any, Dict, List


class ProviderRegistry:

    def __init__(
        self,
        registry_data: Dict[str, Any] | None = None,
    ):

        self.data = registry_data or {}

        self.providers = (
            self.data
            .get("providers", [])
        )


    def get_all(self) -> List[Dict[str, Any]]:

        return self.providers



    def get_by_id(
        self,
        provider_id: str,
    ) -> Dict[str, Any] | None:

        for provider in self.providers:

            if provider.get("id") == provider_id:

                return provider


        return None



    def get_by_category(
        self,
        category: str,
    ) -> List[Dict[str, Any]]:

        return [

            provider

            for provider in self.providers

            if provider.get("category") == category

        ]



    def get_priority_sources(self) -> List[str]:

        priority = (
            self.data
            .get("provider_priority", [])
        )


        return [

            item.get("provider")

            for item in priority

        ]



    def get_reliability(
        self,
        provider_id: str,
    ) -> float:

        provider = self.get_by_id(
            provider_id
        )


        if not provider:

            return 0.0


        return provider.get(
            "reliability_weight",
            0.0
        )



    def supports_authentication(
        self,
        provider_id: str,
    ) -> bool:

        provider = self.get_by_id(
            provider_id
        )


        if not provider:

            return False


        return provider.get(
            "requires_authentication",
            False
        )



    def get_integration_types(
        self,
        provider_id: str,
    ) -> List[str]:

        provider = self.get_by_id(
            provider_id
        )


        if not provider:

            return []


        return provider.get(
            "integration_type",
            []
        )



    def find_capable_provider(
        self,
        capability: str,
    ) -> List[Dict[str, Any]]:

        matches = []


        for provider in self.providers:

            purpose = provider.get(
                "purpose",
                []
            )


            if capability in purpose:

                matches.append(
                    provider
                )


        return matches



    def summary(self) -> Dict[str, Any]:

        return {

            "total_providers":
                len(self.providers),

            "categories":
                list(
                    set(
                        provider.get(
                            "category"
                        )
                        for provider in self.providers
                    )
                ),

            "authenticated_sources":
                len(
                    [
                        p
                        for p in self.providers
                        if p.get(
                            "requires_authentication"
                        )
                    ]
                )

        }