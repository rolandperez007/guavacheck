"""
Government Intelligence Service

Central service layer connecting:

- Registry intelligence
- Provider registry
- Compliance engine
- Verification policy

Provides a unified government intelligence
interface for guavacheck verification workflows.
"""

from typing import Any, Dict, List

from .RegistryLoader import RegistryLoader
from .ProviderRegistry import ProviderRegistry
from .ComplianceEngine import ComplianceEngine
from .GovernmentVerificationPolicy import (
    GovernmentVerificationPolicy,
)


class GovernmentIntelligenceService:

    def __init__(
        self,
        data_path: str | None = None,
    ):

        self.loader = RegistryLoader(
            data_path
        )


        self.data = (
            self.loader.load_all()
        )


        self.provider_registry = (
            ProviderRegistry(
                self.data.get(
                    "providers",
                    {}
                )
            )
        )


        self.compliance = (
            ComplianceEngine(
                self.data.get(
                    "compliance",
                    {}
                )
            )
        )


        self.policy = (
            GovernmentVerificationPolicy(
                self.data.get(
                    "confidence_rules",
                    {}
                )
            )
        )



    def system_status(self) -> Dict[str, Any]:

        return {

            "service":
                "Government Intelligence Service",

            "status":
                "operational",

            "modules":
                self.loader.available_modules(),

            "providers":
                self.provider_registry.summary(),

            "compliance":
                self.compliance.framework_summary()

        }



    def get_country_profile(
        self,
        country_code: str,
    ) -> Dict[str, Any]:

        return {

            "country":
                country_code.upper(),

            "supported":
                self.compliance
                .is_supported_country(
                    country_code
                ),

            "property_requirements":
                self.compliance
                .get_property_requirements(
                    country_code
                ),

            "corporate_requirements":
                self.compliance
                .get_corporate_requirements(
                    country_code
                ),

            "privacy_frameworks":
                self.compliance
                .get_privacy_frameworks(
                    country_code
                )

        }



    def find_verification_sources(
        self,
        capability: str,
    ) -> List[Dict[str, Any]]:

        return (
            self.provider_registry
            .find_capable_provider(
                capability
            )
        )



    def verify_document_requirements(
        self,
        country_code: str,
        documents: List[str],
    ) -> Dict[str, Any]:

        return (
            self.compliance
            .evaluate_property_compliance(
                country_code,
                documents
            )
        )



    def evaluate_verification(
        self,
        score: float,
        evidence_count: int,
        official_sources: int,
    ) -> Dict[str, Any]:

        return (
            self.policy
            .can_issue_certificate(
                score,
                evidence_count,
                official_sources
            )
        )



    def evaluate_transaction(
        self,
        score: float,
        transaction_type: str,
    ) -> Dict[str, Any]:

        return (
            self.policy
            .evaluate_transaction(
                score,
                transaction_type
            )
        )



    def requires_review(
        self,
        property_value_usd: float,
        disputed: bool = False,
        government_asset: bool = False,
    ) -> bool:

        return (
            self.policy
            .requires_manual_review(
                property_value_usd,
                disputed,
                government_asset
            )
        )



    def get_provider_health(self) -> Dict[str, Any]:

        providers = (
            self.provider_registry
            .get_all()
        )


        return {

            "total":
                len(providers),

            "authenticated":

                len(
                    [
                        provider
                        for provider in providers
                        if provider.get(
                            "requires_authentication"
                        )
                    ]
                ),

            "available_categories":

                list(
                    set(
                        provider.get(
                            "category"
                        )
                        for provider in providers
                    )
                )

        }