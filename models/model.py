from config.db import Base
from sqlalchemy import Column, Integer, String

class Task(Base):
    __tablename__ = "Task"
    name = Column(String, primary_key=True)
    description = Column(String)