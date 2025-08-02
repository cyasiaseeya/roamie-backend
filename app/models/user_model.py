from app.models import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    dob = Column(DateTime, nullable = False)
    gender = Column(String, nullable = False)
    email = Column(String, unique = True, index = True, nullable = False)
    password_hash = Column(String, nullable = False)
    profile_photo = Column(String, nullable = True)
