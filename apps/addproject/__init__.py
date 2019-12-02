from flask import Blueprint

addproject = Blueprint('addproject', __name__)

from apps.addproject import views
