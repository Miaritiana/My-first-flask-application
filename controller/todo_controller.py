from flask import Blueprint

from views.todo_view import get_todo, get_one_todo, add_many_todo

app_todo = Blueprint('todo blueprint', __name__)


@app_todo.get('/todo')
def get_all_todo():
    return get_todo()


@app_todo.get('/todo/<todo_id>')
def get_one_todo_by_id(todo_id):
    return get_one_todo(todo_id)


@app_todo.post('/todo')
def add_todo():
    return add_many_todo()
