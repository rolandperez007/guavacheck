from dataclasses import dataclass
from typing import Any


@dataclass
class SecurityContext:
    """
    Core security boundary for multi-tenant execution.
    Prevents cross-user and cross-org data leakage.
    """

    user_id: str
    org_id: str | None = None
    role: str = "user"
    claims: dict[str, Any] | None = None

    def is_admin(self) -> bool:
        return self.role.lower() == "admin"

    def can_access_org(self, org_id: str) -> bool:
        return self.org_id == org_id
