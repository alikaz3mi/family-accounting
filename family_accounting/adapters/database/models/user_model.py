from sqlalchemy import Column, Integer, String, Boolean
from .base import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    phone = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)
    telegram_id = Column(String, nullable=True)
    email = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
