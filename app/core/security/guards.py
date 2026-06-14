from app.core.security.context import SecurityContext


class SecurityGuard:
    @staticmethod
    def validate(context: SecurityContext):
        if context is None:
            raise Exception("SECURITY_ERROR: Missing SecurityContext")

        if not context.user_id:
            raise Exception("SECURITY_ERROR: Missing user_id")

        if not context.org_id:
            raise Exception("SECURITY_ERROR: Missing org_id")

        if context.role not in ["user", "admin", "system"]:
            raise Exception("SECURITY_ERROR: Invalid role")

        return True

    @staticmethod
    def enforce_org_access(context: SecurityContext, org_id: str):
        if context.org_id != org_id and context.role != "admin":
            raise Exception("SECURITY_ERROR: Cross-org access blocked")

        return True
