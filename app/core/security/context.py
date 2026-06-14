from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class SecurityContext:
    """
    Core security boundary for multi-tenant execution.
    Prevents cross-user and cross-org data leakage.
    """

    user_id: str
    org_id: Optional[str] = None
    role: str = "user"
    claims: Optional[Dict[str, Any]] = None

    def is_admin(self) -> bool:
        return self.role.lower() == "admin"

    def can_access_org(self, org_id: str) -> bool:
        return self.org_id == org_id
