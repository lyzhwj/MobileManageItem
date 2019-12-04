from apps import app
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.INTEGER, primary_key=True)
    uname = db.Column(db.String(50), nullable=False)
    nick_name = db.Column(db.String(50), nullable=False)
    pwd = db.Column(db.String(50), nullable=False)
    rid = db.Column(db.INTEGER, nullable=False)
    is_used = db.Column(db.INTEGER, nullable=False)


class Dictionary(db.Model):
    __tablename__ = 't_dict'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    pid = db.Column(db.Integer)
    type = db.Column(db.String(32))

