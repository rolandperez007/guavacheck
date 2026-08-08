from sqlalchemy import text
from app.database.session import engine

with engine.connect() as conn:
    result = conn.execute(
        text("""
        SELECT
            ordinal_position,
            column_name,
            data_type,
            is_nullable
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'users'
        ORDER BY ordinal_position
        """)
    )

    print("\nPUBLIC.USERS — LIVE SCHEMA\n")
    print(
        f"{'POS':<5} "
        f"{'COLUMN':<20} "
        f"{'TYPE':<30} "
        f"{'NULLABLE'}"
    )
    print("-" * 75)

    for row in result:
        print(
            f"{row.ordinal_position:<5} "
            f"{row.column_name:<20} "
            f"{row.data_type:<30} "
            f"{row.is_nullable}"
        )