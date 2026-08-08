from sqlalchemy import text

from app.database.session import engine


def main():
    with engine.connect() as conn:
        print("=== INSTITUTION AUTHORIZATION TABLES ===")

        rows = conn.execute(
            text(
                """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                  AND table_name LIKE 'institution%'
                ORDER BY table_name
                """
            )
        ).fetchall()

        for row in rows:
            print(row.table_name)

        print()
        print("=== ROLE/PERMISSION RELATED TABLES ===")

        rows = conn.execute(
            text(
                """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                  AND (
                      table_name LIKE '%role%'
                      OR table_name LIKE '%permission%'
                      OR table_name LIKE '%membership%'
                  )
                ORDER BY table_name
                """
            )
        ).fetchall()

        for row in rows:
            print(row.table_name)


if __name__ == "__main__":
    main()
