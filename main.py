from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from curd import create_todo, get_todos,get_todo, update_todo, delete_todo

import models
import schemas
import curd

from database import SessionLocal,engine
models.Base.metadata.create_all(bind= engine)

app: FastAPI= FastAPI()

#dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todo")
def add_todo(todo: schemas.TodoCreate, db: Session= Depends(get_db)):
    return create_todo(todo= todo, db= db )

@app.get("/todo")
def api_get_todos(db: Session= Depends(get_db), skip: int= 0, limit:int= 100):
    res = get_todos(db=db,skip=skip, limit=limit)
    return res

@app.get("/todo/id")
def api_get_todo(db: Session = Depends(get_db),id={id}):
    res= get_todo(db=db, id=id)
    return res
@app.put("/todo")

def api_update_too(todo: schemas.TodoUpdate, db:Session = Depends(get_db)):
    return update_todo(db=db, todo=todo)

@app.delete("/todo")
def api_del_todo(todo: schemas.TodoDelete, db: Session= Depends(get_db)):
    return delete_todo(db=db, todo=todo)



