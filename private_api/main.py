# private_api -- this Micro is protected; an admin api for to dos
from deta import Deta
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()

deta = Deta()

todos = deta.Base("my_todos") # separate Base for each installed instance

default_content = "Write code for Space"

class ToDo(BaseModel):
    content: str = default_content
	done: bool = False
    is_public: bool = False

@app.get("/")
def html_handler():
    return HTMLResponse(open("index.html").read())

@app.get("/todos")
def list_todos():
	all_todos = next(todos.fetch([]))
    return all_todos

@app.get("/todos/{todo_key}")
def display_todo():
    return todos.get(todo_id)

@app.post("/todos")
def create_todo(todo: ToDo):
    todo_dict = todo.dict()
    new_todo = todos.put(todo_dict)
    return new_todo

@app.put("/todos/{todo_key}")
def update_todo(todo: ToDo):
    todo_dict = todo.dict()
    updated_todo = todos.put(todo_dict)
    return new_todo

@app.delete("/todos/{todo_key}")
def delete_todo():
    return todos.delete(todo_key)
