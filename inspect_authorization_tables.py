from sqlalchemy import text

from app.database.session import engine


def main():
    with engine.connect() as conn:
        rows = conn.execute(
            text(
                """
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                  AND table_name IN (
                      'roles',
                      'permissions',
                      'user_roles',
                      'role_permissions'
                  )
                ORDER BY table_name
                """
            )
        ).fetchall()

        print("=== AUTHORIZATION TABLES ===")

        for row in rows:
            print(row.table_name)


if __name__ == "__main__":
    main()