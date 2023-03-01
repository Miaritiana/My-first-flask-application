from flask import Blueprint

health_route = Blueprint('health blueprint', __name__)


@health_route.get('/ping')
def health():
    return "pong"
