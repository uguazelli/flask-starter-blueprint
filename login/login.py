from flask import Blueprint

login_blueprint = Blueprint('login_blueprint', __name__)


@login_blueprint.route('/login')
def index():
    return "login page"
