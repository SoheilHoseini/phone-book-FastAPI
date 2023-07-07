from sqlalchemy import Column, Integer, String
from database import Base

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    phone_number = Column(String(11))
