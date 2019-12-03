# coding: utf-8
from apps import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Dictory(db.Model):
    __tablename__ = 't_dict'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    pid = db.Column(db.Integer)



class User(db.Model):
    __tablename__ = 't_user'

    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(32))
    nick_name = db.Column(db.String(32))
    pwd = db.Column(db.String(32))
    rid = db.Column(db.Integer)
    is_used = db.Column(db.Integer)


class Project(db.Model):
    __tablename__ = 't_project'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    catgory = db.Column(db.String(32))
    uid = db.Column(db.ForeignKey('t_user.id'), index=True)
    pre_ini_data = db.DateTime()
    rea_ini_data = db.DateTime()
    rea_end_data = db.DateTime()
    status = db.Column(db.Integer)
    total_account = db.Column(db.FLOAT)

    t_user = db.relationship('TUser')
    t_user1 = db.relationship('TUser', secondary='t_sp')


class History(db.Model):
    __tablename__ = 't_history'

    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.ForeignKey('t_project.id'), index=True)
    info = db.Column(db.String(500))
    staus = db.Column(db.Integer)
    uid = db.Column(db.ForeignKey('t_user.id'), index=True)

    t_project = db.relationship('Project')
    t_user = db.relationship('User')


t_t_sp = db.Table(
    't_sp', db.metadata,
    db.Column('pid', db.ForeignKey('t_project.id'), primary_key=True, nullable=False),
    db.Column('uid', db.ForeignKey('t_user.id'), primary_key=True, nullable=False, index=True)
)
