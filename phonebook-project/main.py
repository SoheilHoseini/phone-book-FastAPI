from fastapi import FastAPI, status
from database import Base, engine, ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session


# Create ToDoRequest Base Model => I think it determines how a new record should be created
class ToDoRequest(BaseModel):
    task: str


# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

@app.get("/")
def root():
    return "todooo"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo(todo: ToDoRequest):
    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    tododb = ToDo(task = todo.task)

    # add it to the session and commit it
    session.add(tododb)
    session.commit()

    # grab the id given to the object from the database
    id = tododb.id

    # close the session
    session.close()

    # return the id
    return f"created todo item with id {id}"

@app.get("/todo/{id}")
def read_todo(id: int):
    return f"read todo item with id {id}"

@app.put("/todo/{id}")
def update_todo(id: int):
    return f"update todo item with id {id}"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    return f"delete todo item with id {id}"

@app.get("/todo")
def read_todo_list():
    return "read todo list"
