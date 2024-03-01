from flask import Blueprint

home_blueprint = Blueprint('home', __name__)


@home_blueprint.route('/', methods=['GET'])
def get_users():
    return "hey there!"
