from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

db = SQLAlchemy()


class Todo(db.Model):
    db.Table('todo', MetaData())

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String())
    is_checked = db.Column(db.Boolean())

    def __init__(self, id, description, is_checked):
        self.id = id
        self.description = description
        self.is_checked = is_checked

    def __repr__(self):
        return f"<Todo {self.id}>"
