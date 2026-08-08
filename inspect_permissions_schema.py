from sqlalchemy import text

from app.database.session import engine


def main():
    with engine.connect() as conn:
        rows = conn.execute(
            text(
                """
                SELECT
                    ordinal_position,
                    column_name,
                    data_type,
                    is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'public'
                  AND table_name = 'permissions'
                ORDER BY ordinal_position
                """
            )
        ).fetchall()

        print("=== PUBLIC.PERMISSIONS — LIVE SCHEMA ===")

        for row in rows:
            print(
                f"{row.ordinal_position} | "
                f"{row.column_name} | "
                f"{row.data_type} | "
                f"nullable={row.is_nullable}"
            )


if __name__ == "__main__":
    main()