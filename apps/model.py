from flask_sqlalchemy import SQLAlchemy
from apps import app
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)