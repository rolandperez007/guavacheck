from .base_template import BaseWorkflowTemplate
from .registry import WorkflowTemplateRegistry

from .property_verification import PropertyVerificationTemplate
from .property_purchase import PropertyPurchaseTemplate
from .property_sale import PropertySaleTemplate
from .mortgage_approval import MortgageApprovalTemplate
from .loan_origination import LoanOriginationTemplate
from .insurance_claim import InsuranceClaimTemplate
from .tenant_screening import TenantScreeningTemplate
from .construction_approval import ConstructionApprovalTemplate
from .developer_onboarding import DeveloperOnboardingTemplate
from .property_transfer import PropertyTransferTemplate
from .rent_collection import RentCollectionTemplate
from .maintenance_request import MaintenanceRequestTemplate
from .institution_onboarding import InstitutionOnboardingTemplate

__all__ = [
    "BaseWorkflowTemplate",
    "WorkflowTemplateRegistry",
    "PropertyVerificationTemplate",
    "PropertyPurchaseTemplate",
    "PropertySaleTemplate",
    "MortgageApprovalTemplate",
    "LoanOriginationTemplate",
    "InsuranceClaimTemplate",
    "TenantScreeningTemplate",
    "ConstructionApprovalTemplate",
    "DeveloperOnboardingTemplate",
    "PropertyTransferTemplate",
    "RentCollectionTemplate",
    "MaintenanceRequestTemplate",
    "InstitutionOnboardingTemplate",
]