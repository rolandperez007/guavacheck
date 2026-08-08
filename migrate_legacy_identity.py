from sqlalchemy import text

from app.database.session import engine


def migrate():
    with engine.begin() as conn:

        print("\n=== GuavaCheck Legacy Identity Migration ===\n")

        # ---------------------------------------------------------
        # Find users that do not yet have an identity.
        # ---------------------------------------------------------

        users = conn.execute(
            text("""
                SELECT id, email, phone
                FROM public.users
                WHERE identity_id IS NULL
                ORDER BY created_at
            """)
        ).fetchall()

        if not users:
            print("No users require identity migration.")
            return

        for user in users:

            print(f"Processing: {user.email}")

            # -----------------------------------------------------
            # Find an existing identity with the same email.
            # -----------------------------------------------------

            identity = conn.execute(
                text("""
                    SELECT id
                    FROM public.identities
                    WHERE LOWER(email) = LOWER(:email)
                    LIMIT 1
                """),
                {"email": user.email},
            ).fetchone()

            if identity:
                identity_id = identity.id

                print(
                    f"Existing identity found: {identity_id}"
                )

            else:
                # -------------------------------------------------
                # Create identity for the legacy user.
                # PostgreSQL generates the UUID.
                # -------------------------------------------------

                identity_id = conn.execute(
                    text("""
                        INSERT INTO public.identities (
                            id,
                            email,
                            phone,
                            identity_type,
                            status,
                            created_at
                        )
                        VALUES (
                            gen_random_uuid()::text,
                            :email,
                            :phone,
                            'individual',
                            'active',
                            NOW()
                        )
                        RETURNING id
                    """),
                    {
                        "email": user.email,
                        "phone": user.phone,
                    },
                ).scalar_one()

                print(
                    f"Created identity: {identity_id}"
                )

            # -----------------------------------------------------
            # Link the user to the identity.
            # -----------------------------------------------------

            conn.execute(
                text("""
                    UPDATE public.users
                    SET identity_id = :identity_id
                    WHERE id = :user_id
                """),
                {
                    "identity_id": identity_id,
                    "user_id": user.id,
                },
            )

            print(
                f"Linked user {user.id} → {identity_id}"
            )

        # ---------------------------------------------------------
        # Verify migration.
        # ---------------------------------------------------------

        result = conn.execute(
            text("""
                SELECT
                    u.id,
                    u.email,
                    u.identity_id,
                    i.email AS identity_email
                FROM public.users u
                LEFT JOIN public.identities i
                    ON i.id = u.identity_id
                ORDER BY u.created_at
            """)
        )

        print("\n=== Identity Relationships ===\n")

        for row in result:
            print(
                f"user={row.id} | "
                f"user_email={row.email} | "
                f"identity_id={row.identity_id} | "
                f"identity_email={row.identity_email}"
            )

        print("\n=== Legacy Identity Migration Complete ===")


if __name__ == "__main__":
    migrate()