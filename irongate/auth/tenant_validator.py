# irongate/auth/tenant_validator.py


def validate_tenant(context):
    tenant = context.get("tenant")

    if not tenant:
        return False, "tenant missing"

    return True, None
