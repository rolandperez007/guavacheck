"""
Compliance Engine

Evaluates country regulatory requirements,
privacy obligations, government readiness,
and enterprise compliance requirements
for guavacheck verification workflows.
"""

from typing import Any, Dict, List


class ComplianceEngine:

    def __init__(
        self,
        compliance_data: Dict[str, Any] | None = None,
    ):

        self.data = compliance_data or {}

        self.countries = (
            self.data
            .get("countries", [])
        )

        self.frameworks = (
            self.data
            .get("global_standards", [])
        )

        self.contract_requirements = (
            self.data
            .get(
                "government_contract_requirements",
                {}
            )
        )



    def get_country(
        self,
        country_code: str,
    ) -> Dict[str, Any] | None:

        code = country_code.upper()


        for country in self.countries:

            if country.get("code") == code:

                return country


        return None



    def is_supported_country(
        self,
        country_code: str,
    ) -> bool:

        return (
            self.get_country(
                country_code
            )
            is not None
        )



    def get_privacy_frameworks(
        self,
        country_code: str,
    ) -> List[str]:

        country = self.get_country(
            country_code
        )


        if not country:

            return []


        return country.get(
            "privacy_framework",
            []
        )



    def get_property_requirements(
        self,
        country_code: str,
    ) -> Dict[str, Any]:

        country = self.get_country(
            country_code
        )


        if not country:

            return {}


        return country.get(
            "property_compliance",
            {}
        )



    def get_corporate_requirements(
        self,
        country_code: str,
    ) -> Dict[str, Any]:

        country = self.get_country(
            country_code
        )


        if not country:

            return {}


        return country.get(
            "corporate_compliance",
            {}
        )



    def government_ready(
        self,
        country_code: str,
    ) -> bool:

        country = self.get_country(
            country_code
        )


        if not country:

            return False


        return country.get(
            "government_ready",
            False
        )



    def required_security_controls(self) -> List[str]:

        return self.contract_requirements.get(
            "required_capabilities",
            []
        )



    def minimum_security_level(self) -> str:

        return self.contract_requirements.get(
            "minimum_security_level",
            "standard"
        )



    def validate_contract_readiness(
        self,
        country_code: str,
        security_features: List[str],
    ) -> Dict[str, Any]:

        country_ready = self.government_ready(
            country_code
        )


        required = (
            self.required_security_controls()
        )


        missing = [

            feature

            for feature in required

            if feature not in security_features

        ]


        return {

            "country_supported":
                country_ready,

            "security_level":
                self.minimum_security_level(),

            "required_controls":
                required,

            "missing_controls":
                missing,

            "ready_for_contract":
                country_ready
                and len(missing) == 0

        }



    def evaluate_property_compliance(
        self,
        country_code: str,
        documents: List[str],
    ) -> Dict[str, Any]:

        requirements = (
            self.get_property_requirements(
                country_code
            )
        )


        required_documents = (
            requirements
            .get(
                "required_documents",
                []
            )
        )


        missing = [

            document

            for document in required_documents

            if document not in documents

        ]


        return {

            "required_documents":
                required_documents,

            "submitted_documents":
                documents,

            "missing_documents":
                missing,

            "compliance_score":
                self._calculate_score(
                    len(required_documents),
                    len(missing)
                )

        }



    def _calculate_score(
        self,
        total: int,
        missing: int,
    ) -> float:

        if total == 0:

            return 100.0


        completed = total - missing


        return round(
            (completed / total) * 100,
            2
        )



    def framework_summary(self) -> Dict[str, Any]:

        return {

            "global_framework_count":
                len(self.frameworks),

            "supported_countries":
                len(self.countries),

            "government_ready_countries":
                len(
                    [
                        country
                        for country in self.countries
                        if country.get(
                            "government_ready"
                        )
                    ]
                )

        }