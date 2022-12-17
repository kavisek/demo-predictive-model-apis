from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker

# Postgres URL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:docker@localhost/postgres"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # specify schema
    connect_args={"options": "-csearch_path=public"}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DBContext:
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, et, ev, traceback):
        self.db.close()