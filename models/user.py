from database import Base, Session
from sqlalchemy import Column, Integer, String, DateTime, func
class User(Base):
    __tablename__ = 'users'

    telegram_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    campaign = Column(String)
    language = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# async def create_user(user: User):
#     with Session() as session:
#         session.add(user)
#         session.commit()
#
# async def update_user(user: User):
#     with Session() as session:
#         session.add(user)
#         session.commit()


    