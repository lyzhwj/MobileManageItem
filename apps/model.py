from apps import app
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nick_name = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(50), nullable=False)
    rid = db.Column(db.INTEGER,nullable=False)
    is_used = db.Column(db.INTEGER,nullable=False)
    regis_date = db.Column(db.DateTime, nullable=False)



