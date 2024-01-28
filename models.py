from database import Base
from sqlalchemy import Integer, Column, String

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key= True) # Here primary Key is small in letters
    text= Column(String)