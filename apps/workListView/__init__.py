from flask import Blueprint

wkl = Blueprint('workListView', __name__)

from apps.workListView import view
