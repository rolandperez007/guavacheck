from sqlalchemy import text

from app.database.session import engine


def main():
    with engine.connect() as conn:

        print("=== ROLE_PERMISSIONS — LIVE SCHEMA ===")

        columns = conn.execute(
            text(
                """
                SELECT
                    ordinal_position,
                    column_name,
                    data_type,
                    is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'public'
                  AND table_name = 'role_permissions'
                ORDER BY ordinal_position
                """
            )
        ).fetchall()

        for row in columns:
            print(
                f"{row.ordinal_position} | "
                f"{row.column_name} | "
                f"{row.data_type} | "
                f"nullable={row.is_nullable}"
            )

        print()
        print("=== ROLE_PERMISSIONS — DATA ===")

        rows = conn.execute(
            text(
                """
                SELECT *
                FROM public.role_permissions
                ORDER BY 1, 2
                """
            )
        ).fetchall()

        if not rows:
            print("No role-permission assignments found.")
        else:
            for row in rows:
                print(row)


if __name__ == "__main__":
    main()