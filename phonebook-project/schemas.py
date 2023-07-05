from pydantic import BaseModel

# Create ToDo Schema (Pydantic Model)
class ToDo(BaseModel):
    task: str
