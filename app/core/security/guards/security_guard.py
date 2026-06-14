@"
from app.core.security.context import SecurityContext


class SecurityGuard:
    """
    Central enforcement layer for all execution paths.
    Prevents:
    - cross-org access
    - invalid roles
    - unauthorized system actions
    """

    @staticmethod
    def enforce(context: SecurityContext, org_id: str = None):

        if context is None:
            raise Exception("SECURITY_ERROR: Missing SecurityContext")

        if not context.user_id:
            raise Exception("SECURITY_ERROR: Missing user_id")

        if not context.org_id:
            raise Exception("SECURITY_ERROR: Missing org_id")

        # 🔐 ORG ISOLATION
        if org_id and context.org_id != org_id:
            if context.role != "admin":
                raise Exception("SECURITY_ERROR: Cross-org access blocked")

        # 🔐 ROLE VALIDATION
        if context.role not in ["user", "admin", "system"]:
            raise Exception("SECURITY_ERROR: Invalid role")

        return True
"@ | Set-Content -Encoding UTF8 app\core\security\guards\security_guard.py