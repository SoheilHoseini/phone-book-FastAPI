from fastapi import FastAPI, status
from database import Base, engine

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

@app.get("/")
def root():
    return "todooo"

@app.post("/todo", status_code=status.HTTP_201_CREATED)
def create_todo():
    return "create todo item"

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
