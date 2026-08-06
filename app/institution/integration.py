"""
Institution Integration Registry.

Acts as the central coordination point
between the Institution Platform and
other Guava engines.
"""

from app.institution.adapters.passport_adapter import PassportAdapter
from app.institution.adapters.twin_adapter import TwinAdapter
from app.institution.adapters.vision_adapter import VisionAdapter
from app.institution.adapters.billing_adapter import BillingAdapter
from app.institution.adapters.austin_adapter import AustinAdapter
from app.institution.adapters.decision_adapter import DecisionAdapter
from app.institution.adapters.trust_adapter import TrustAdapter
from app.institution.adapters.notification_adapter import NotificationAdapter


class InstitutionIntegration:

    def __init__(self) -> None:
        self.passport = PassportAdapter()
        self.twin = TwinAdapter()
        self.vision = VisionAdapter()
        self.billing = BillingAdapter()
        self.austin = AustinAdapter()
        self.decision = DecisionAdapter()
        self.trust = TrustAdapter()
        self.notifications = NotificationAdapter()