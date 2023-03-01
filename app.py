from flask import Flask
from flask_migrate import Migrate

from controller.health_controller import health_route
from controller.todo_controller import app_todo
from models.todo import db

# Database connection
app = Flask(__name__)
app.register_blueprint(app_todo)
app.register_blueprint(health_route)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/todo_list"
db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
