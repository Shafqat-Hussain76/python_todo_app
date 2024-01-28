from sqlalchemy.orm import Session
import models
import schemas 
from sqlalchemy import text
from database import engine

def get_todo(db: Session, id:int):
    return db.query(models.Todo).filter(models.Todo.id == id).first()


def get_todos(db:Session, skip: int= 0, limit:int= 100):
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM Todo"))
        print(result.all())
    #return db.query(models.Todo).offset(skip).limit(limit).all()

def create_todo(db:Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(text  = todo.text)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return "Todo has been added...."

def update_todo(db: Session, todo: schemas.TodoUpdate):
    val = db.query(models.Todo).filter(models.Todo.id == todo.id).first()
    val.text = todo.text
    db.add(val)
    db.commit()
    db.refresh(val)
    return "updated"

def delete_todo(db: Session, todo: schemas.TodoDelete) -> str:
    val = db.query(models.Todo).filter(models.Todo.id == todo.id).first()
    db.delete(val)
    db.commit()
    
    return "Deleted"

