from .database import Base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = '_user'
    id = Column(Integer, primary_key = True, index = True, autoincrement=True)
    email = Column(String, unique = True)
    password = Column(String)
    name = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
