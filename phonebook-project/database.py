from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a sqlite engine instance
engine = create_engine("sqlite:///todooo.db")

# Create a DeclarativeMeta instance
Base = declarative_base()

# Define To Do class inheriting from Base
class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    task = Column(String(256))
