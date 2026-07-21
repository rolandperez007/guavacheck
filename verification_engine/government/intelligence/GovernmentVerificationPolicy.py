"""
Government Verification Policy

Defines operational rules for government-grade
property verification, certificate issuance,
risk escalation and institutional requirements.
"""

from typing import Any, Dict


class GovernmentVerificationPolicy:

    def __init__(
        self,
        policy_data: Dict[str, Any] | None = None,
    ):

        self.data = policy_data or {}

        self.policy = (
            self.data
            .get(
                "verification_policy",
                {}
            )
        )

        self.institutional = (
            self.data
            .get(
                "institutional_policy",
                {}
            )
        )

        self.trust_levels = (
            self.data
            .get(
                "trust_levels",
                []
            )
        )



    def minimum_confidence_score(self) -> float:

        return self.policy.get(
            "minimum_confidence_score",
            75
        )



    def requires_official_source(self) -> bool:

        return self.policy.get(
            "official_source_required",
            True
        )



    def requires_multiple_sources(self) -> bool:

        return self.policy.get(
            "multiple_source_confirmation",
            True
        )



    def get_trust_level(
        self,
        score: float,
    ) -> Dict[str, Any]:

        matched = {

            "level": "UNKNOWN",

            "meaning":
                "Verification level not determined"

        }


        for level in self.trust_levels:

            minimum = level.get(
                "minimum_score",
                0
            )


            if score >= minimum:

                matched = level

                break


        return matched



    def can_issue_certificate(
        self,
        score: float,
        evidence_count: int,
        official_sources: int,
    ) -> Dict[str, Any]:

        minimum_score = (
            self.minimum_confidence_score()
        )


        checks = {

            "score_passed":
                score >= minimum_score,

            "evidence_available":
                evidence_count > 0,

            "official_source_available":
                official_sources > 0

        }


        passed = all(
            checks.values()
        )


        return {

            "approved":
                passed,

            "checks":
                checks,

            "trust_level":
                self.get_trust_level(
                    score
                )

        }



    def requires_manual_review(
        self,
        property_value_usd: float,
        disputed: bool = False,
        government_asset: bool = False,
    ) -> bool:

        threshold = (
            self.institutional
            .get(
                "require_manual_review_above_value_usd",
                5000000
            )
        )


        if property_value_usd >= threshold:

            return True


        if disputed:

            return True


        if government_asset:

            return True


        return False



    def investment_threshold(self) -> float:

        return self.institutional.get(
            "minimum_score_for_investment",
            85
        )



    def mortgage_threshold(self) -> float:

        return self.institutional.get(
            "minimum_score_for_mortgage",
            90
        )



    def government_contract_threshold(self) -> float:

        return self.institutional.get(
            "minimum_score_for_government_contracts",
            95
        )



    def evaluate_transaction(
        self,
        score: float,
        transaction_type: str,
    ) -> Dict[str, Any]:

        transaction_type = (
            transaction_type.lower()
        )


        thresholds = {

            "investment":
                self.investment_threshold(),

            "mortgage":
                self.mortgage_threshold(),

            "government":
                self.government_contract_threshold(),

        }


        required = thresholds.get(
            transaction_type,
            self.minimum_confidence_score()
        )


        return {

            "transaction_type":
                transaction_type,

            "required_score":
                required,

            "current_score":
                score,

            "approved":
                score >= required,

            "trust_level":
                self.get_trust_level(
                    score
                )

        }