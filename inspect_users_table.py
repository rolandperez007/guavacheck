from sqlalchemy import text
from app.database.session import engine

with engine.connect() as conn:
    result = conn.execute(
        text("""
        SELECT
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'users'
        ORDER BY ordinal_position
        """)
    )

    print("\nUsers table:\n")

    for row in result:
        print(row.column_name, "-", row.data_type)