# Blueprint for user-related API routes

from flask import Blueprint

user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/', methods=['GET'])
def get_users():
    return "List of users"
