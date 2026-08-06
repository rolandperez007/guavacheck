"""
Institution orchestration layer.

Coordinates workflows spanning multiple
Guava bounded contexts.

This package contains business processes,
not persistence models.
"""

from .coordinator import InstitutionCoordinator
from .onboarding import InstitutionOnboardingWorkflow
from .mortgage import MortgageWorkflow
from .verification import VerificationWorkflow
from .property_sale import PropertySaleWorkflow
from .valuation import ValuationWorkflow
from .insurance import InsuranceWorkflow
from .compliance import ComplianceWorkflow

__all__ = [
    "InstitutionCoordinator",
    "InstitutionOnboardingWorkflow",
    "MortgageWorkflow",
    "VerificationWorkflow",
    "PropertySaleWorkflow",
    "ValuationWorkflow",
    "InsuranceWorkflow",
    "ComplianceWorkflow",
]