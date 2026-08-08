from app.database.session import engine
from sqlalchemy import text


print("=== GuavaCheck Users → Identity Foreign Key Migration ===")

with engine.begin() as conn:

    print("\n[1] Checking for orphaned identity references...")

    orphaned = conn.execute(
        text("""
            SELECT u.id, u.identity_id
            FROM public.users u
            LEFT JOIN public.identities i
                ON i.id = u.identity_id
            WHERE u.identity_id IS NOT NULL
              AND i.id IS NULL
        """)
    ).fetchall()

    if orphaned:
        print("ERROR: Orphaned identity references found.")

        for row in orphaned:
            print(
                f"user_id={row.id} | "
                f"identity_id={row.identity_id}"
            )

        raise RuntimeError(
            "Cannot create foreign key while orphaned references exist."
        )

    print("No orphaned identity references found.")

    print("\n[2] Checking existing foreign keys...")

    existing = conn.execute(
        text("""
            SELECT constraint_name
            FROM information_schema.table_constraints
            WHERE constraint_schema = 'public'
              AND table_name = 'users'
              AND constraint_type = 'FOREIGN KEY'
        """)
    ).fetchall()

    identity_fk_exists = False

    for row in existing:
        print(f"Existing FK: {row.constraint_name}")

        columns = conn.execute(
            text("""
                SELECT column_name
                FROM information_schema.key_column_usage
                WHERE constraint_schema = 'public'
                  AND constraint_name = :constraint_name
            """),
            {"constraint_name": row.constraint_name},
        ).fetchall()

        for column in columns:
            if column.column_name == "identity_id":
                identity_fk_exists = True

    if identity_fk_exists:
        print("\nidentity_id foreign key already exists.")
    else:
        print("\n[3] Creating identity_id foreign key...")

        conn.execute(
            text("""
                ALTER TABLE public.users
                ADD CONSTRAINT users_identity_id_fkey
                FOREIGN KEY (identity_id)
                REFERENCES public.identities(id)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
            """)
        )

        print("Foreign key created successfully.")

    print("\n[4] Verifying relationship...")

    result = conn.execute(
        text("""
            SELECT
                u.id AS user_id,
                u.identity_id,
                i.id AS identity_id,
                i.email
            FROM public.users u
            LEFT JOIN public.identities i
                ON i.id = u.identity_id
            WHERE u.identity_id IS NOT NULL
            ORDER BY u.created_at
        """)
    )

    for row in result:
        print(
            f"user={row.user_id} | "
            f"user.identity_id={row.identity_id} | "
            f"identity.id={row.identity_id} | "
            f"email={row.email}"
        )


print("\n=== Users → Identity Foreign Key Migration Complete ===")
