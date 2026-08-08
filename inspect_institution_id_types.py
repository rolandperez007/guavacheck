from sqlalchemy import text
from app.database.session import engine

tables = [
    "users",
    "institutions",
    "institution_memberships",
    "institution_roles",
    "institution_permissions",
    "institution_role_permissions",
    "institution_membership_roles",
]

with engine.connect() as conn:
    for table in tables:
        print(f"\n=== {table.upper()} ===")

        result = conn.execute(
            text("""
                SELECT
                    column_name,
                    data_type,
                    udt_name,
                    is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'public'
                  AND table_name = :table
                ORDER BY ordinal_position
            """),
            {"table": table},
        )

        rows = result.fetchall()

        if not rows:
            print("TABLE DOES NOT EXIST")
        else:
            for row in rows:
                print(
                    f"{row.column_name} | "
                    f"{row.data_type} | "
                    f"{row.udt_name} | "
                    f"nullable={row.is_nullable}"
                )
