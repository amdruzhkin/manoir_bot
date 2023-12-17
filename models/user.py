from database import Base
from sqlalchemy import Column, Integer, String, DateTime, func
class User(Base):
    __tablename__ = 'users'
    tg_id = Column(Integer, primary_key=True, index=True)
    tg_username = Column(String, unique=True, index=True)
    real_name = Column(String)
    campaign = Column(String)
    language = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
