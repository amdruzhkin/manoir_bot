from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *
from contextlib import contextmanager

DB_URL = "sqlite:///./manoir.db"

Engine = create_engine(DB_URL, connect_args={"check_same_thread": False}, echo=True)
SessionLocal = sessionmaker(bind=Engine, autocommit=False, autoflush=False, expire_on_commit=False)
Base = declarative_base()

@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

if __name__ == '__main__':
    tabs = [User.__table__]
    Base.metadata.create_all(Engine, tables=tabs)