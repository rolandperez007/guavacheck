import os

DATABASE_URL = os.getenv("DATABASE_URL")

engine = None

if DATABASE_URL:
    from sqlalchemy import create_engine
    engine = create_engine(DATABASE_URL)