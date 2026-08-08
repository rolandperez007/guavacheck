from app.database.session import engine
from sqlalchemy import text


print("=== GuavaCheck Users / Identity Verification ===")

with engine.connect() as conn:

    print("\n[1] PUBLIC.USERS COLUMNS")

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

    for row in result:
        print(
            f"{row.ordinal_position} | "
            f"{row.column_name} | "
            f"{row.data_type} | "
            f"nullable={row.is_nullable}"
        )


    print("\n[2] USER → IDENTITY RELATIONSHIP")

    result = conn.execute(
        text("""
            SELECT
                u.id AS user_id,
                u.identity_id,
                u.username,
                u.status,
                i.id AS identity_record_id,
                i.email AS identity_email
            FROM public.users u
            LEFT JOIN public.identities i
                ON i.id = u.identity_id
            ORDER BY u.created_at
        """)
    )

    for row in result:
        print(
            f"user_id={row.user_id} | "
            f"identity_id={row.identity_id} | "
            f"username={row.username} | "
            f"status={row.status} | "
            f"identity_record_id={row.identity_record_id} | "
            f"identity_email={row.identity_email}"
        )


    print("\n[3] FOREIGN KEY CHECK")

    result = conn.execute(
        text("""
            SELECT
                tc.constraint_name,
                kcu.column_name,
                ccu.table_schema AS foreign_table_schema,
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name
            FROM information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
            JOIN information_schema.constraint_column_usage AS ccu
                ON ccu.constraint_name = tc.constraint_name
                AND ccu.table_schema = tc.table_schema
            WHERE tc.constraint_type = 'FOREIGN KEY'
              AND tc.table_schema = 'public'
              AND tc.table_name = 'users'
              AND kcu.column_name = 'identity_id'
        """)
    )

    rows = result.fetchall()

    if rows:
        for row in rows:
            print(
                f"{row.constraint_name} | "
                f"{row.column_name} → "
                f"{row.foreign_table_schema}.{row.foreign_table_name}."
                f"{row.foreign_column_name}"
            )
    else:
        print("WARNING: identity_id foreign key was NOT found.")


    print("\n[4] ROLAND ACCOUNT CHECK")

    result = conn.execute(
        text("""
            SELECT
                u.id,
                u.username,
                u.identity_id,
                u.status,
                i.email
            FROM public.users u
            LEFT JOIN public.identities i
                ON i.id = u.identity_id
            WHERE u.id = '7eb5f9ce-67ed-4ac2-812d-c91699503b12'
        """)
    )

    row = result.fetchone()

    if row:
        print(
            f"user_id={row.id} | "
            f"username={row.username} | "
            f"identity_id={row.identity_id} | "
            f"status={row.status} | "
            f"email={row.email}"
        )
    else:
        print("WARNING: Roland account was not found.")


print("\n=== Verification Complete ===")