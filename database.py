from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from models import *

DB_URL = "sqlite:///./manoir.db"

Engine = create_engine(DB_URL, connect_args={"check_same_thread": False}, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()

if __name__ == '__main__':
    tabs = [User.__tablename__]
    Base.metadata.create_all(Engine, tables=tabs)