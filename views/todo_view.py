from flask import request

from models.todo import Todo, db


def get_todo():
    tasks = Todo.query.all()
    results = [
        {
            "description": task.description,
            "isChecked": task.is_checked
        } for task in tasks
    ]

    return results


def get_one_todo(id_todo: int):
    task = Todo.query.get(id_todo)
    result = {
        "description": task.description,
        "isChecked": task.is_checked
    }

    return result


def add_many_todo():
    if request.is_json:
        data = request.get_json()
        new_todo = [Todo(id=each_data["id"],
                         description=each_data["description"],
                         is_checked=each_data["isChecked"])
                    for each_data in data]
        db.session.add_all(new_todo)
        db.session.commit()
        tasks = Todo.query.all()
        results = [
            {
                "description": task.description,
                "isChecked": task.is_checked
            } for task in tasks
        ]

        return results

