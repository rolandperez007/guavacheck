from sqlalchemy import text

from app.db.session import SessionLocal


def create_user(email: str, full_name: str):
    db = SessionLocal()

    query = text("""
        INSERT INTO users (email, full_name)
        VALUES (:email, :full_name)
        RETURNING id
    """)

    result = db.execute(query, {"email": email, "full_name": full_name})
    db.commit()

    return result.fetchone()[0]
