from database import get_session
from models import User

async def get_user_by_id(tg_id):
    with get_session() as session:
        return session.query(User).filter(User.tg_id == tg_id).first()
async def create_user(user: User):
    with get_session() as session:
        session.add(user)
        session.commit()

async def update_user(user: User):
    with get_session() as session:
        session.add(user)
        session.commit()