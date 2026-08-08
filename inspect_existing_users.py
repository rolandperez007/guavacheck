from sqlalchemy import text
from app.database.session import engine

with engine.connect() as conn:
    result = conn.execute(
        text("""
        SELECT *
        FROM public.users
        ORDER BY created_at
        """)
    )

    columns = result.keys()

    print("\nExisting users:\n")
    print(" | ".join(columns))
    print("-" * 120)

    for row in result:
        print(" | ".join(str(value) for value in row))