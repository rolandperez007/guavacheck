from sqlalchemy import text

from app.database.session import engine


def migrate():
    with engine.begin() as conn:

        print("\n=== GuavaCheck Users Identity Migration ===\n")

        # ---------------------------------------------------------
        # 1. Add identity_id if it does not already exist
        # ---------------------------------------------------------

        conn.execute(
            text("""
                ALTER TABLE public.users
                ADD COLUMN IF NOT EXISTS identity_id VARCHAR(36)
            """)
        )

        print("[1/6] identity_id column ready.")

        # ---------------------------------------------------------
        # 2. Add username if it does not already exist
        # ---------------------------------------------------------

        conn.execute(
            text("""
                ALTER TABLE public.users
                ADD COLUMN IF NOT EXISTS username VARCHAR(100)
            """)
        )

        print("[2/6] username column ready.")

        # ---------------------------------------------------------
        # 3. Add status if it does not already exist
        # ---------------------------------------------------------

        conn.execute(
            text("""
                ALTER TABLE public.users
                ADD COLUMN IF NOT EXISTS status VARCHAR(50)
            """)
        )

        print("[3/6] status column ready.")

        # ---------------------------------------------------------
        # 4. Populate identity_id by matching email
        #
        # Only identities with matching email addresses are linked.
        # Existing users without a matching identity remain NULL.
        # ---------------------------------------------------------

        conn.execute(
            text("""
                UPDATE public.users u
                SET identity_id = i.id
                FROM public.identities i
                WHERE LOWER(u.email) = LOWER(i.email)
                  AND u.identity_id IS NULL
            """)
        )

        print("[4/6] Existing users linked to matching identities.")

        # ---------------------------------------------------------
        # 5. Populate username and status for legacy users
        # ---------------------------------------------------------

        conn.execute(
            text("""
                UPDATE public.users
                SET
                    username = COALESCE(
                        NULLIF(username, ''),
                        SPLIT_PART(email, '@', 1)
                    ),
                    status = CASE
                        WHEN active = TRUE THEN 'active'
                        ELSE 'inactive'
                    END
                WHERE username IS NULL
                   OR status IS NULL
            """)
        )

        print("[5/6] username and status populated.")

        # ---------------------------------------------------------
        # 6. Report migration state
        # ---------------------------------------------------------

        result = conn.execute(
            text("""
                SELECT
                    id,
                    email,
                    identity_id,
                    username,
                    status
                FROM public.users
                ORDER BY created_at
            """)
        )

        print("\n=== Users After Migration ===\n")

        for row in result:
            print(
                f"id={row.id} | "
                f"email={row.email} | "
                f"identity_id={row.identity_id} | "
                f"username={row.username} | "
                f"status={row.status}"
            )

        print("\n=== Migration Preparation Complete ===")


if __name__ == "__main__":
    migrate()