from pydantic import BaseModel

class TodoCreate(BaseModel):
    text: str # here we use : not = sign as we did in models.py file
    
class TodoUpdate(BaseModel):
    id: int
    text: str

class TodoDelete(BaseModel):
    id: int
    