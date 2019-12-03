from flask.blueprints import Blueprint

user_bp = Blueprint('user', __name__)
category_bp = Blueprint('category', __name__)

from apps.user import view
