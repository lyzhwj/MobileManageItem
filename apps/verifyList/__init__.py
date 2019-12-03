from flask.blueprints import Blueprint

verify = Blueprint('verifyList', __name__)

from apps.verifyList import view
