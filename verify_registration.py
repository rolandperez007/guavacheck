from app.database.session import engine
from sqlalchemy import text


with engine.connect() as conn:
    rows = conn.execute(
        text(
            """
            SELECT
                u.id AS user_id,
                u.email AS user_email,
                u.username,
                u.identity_id,
                u.status,
                i.id AS identity_record_id,
                i.email AS identity_email,
                i.identity_type,
                i.status AS identity_status
            FROM public.users u
            LEFT JOIN public.identities i
                ON u.identity_id = i.id
            ORDER BY u.created_at
            """
        )
    ).fetchall()

    print("=== GuavaCheck Registration Verification ===")

    for row in rows:
        print(
            f"user_id={row.user_id} | "
            f"email={row.user_email} | "
            f"username={row.username} | "
            f"identity_id={row.identity_id} | "
            f"status={row.status} | "
            f"identity_record_id={row.identity_record_id} | "
            f"identity_email={row.identity_email} | "
            f"identity_type={row.identity_type} | "
            f"identity_status={row.identity_status}"
        )

    print("=== Verification Complete ===")