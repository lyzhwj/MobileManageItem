# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from apps import app

db = SQLAlchemy(app)


class Dictory(db.Model):
    __tablename__ = 't_dict'

    name = db.Column(db.String(32), primary_key=True)
    pid = db.Column(db.INTEGER, primary_key=True)


class User(db.Model):
    __tablename__ = 't_user'

    id = db.Column(db.INTEGER, primary_key=True)
    uname = db.Column(db.String(32))
    nick_name = db.Column(db.String(32))
    pwd = db.Column(db.String(32))
    rid = db.Column(db.INTEGER)
    is_used = db.Column(db.INTEGER)


class Project(db.Model):
    __tablename__ = 't_project'

    id = db.Column(db.INTEGER, primary_key=True)
    # ptime = db.Column(DATETIME, default=datetime.now())
    name = db.Column(db.String(32))
    info = db.Column(db.String(32))
    uid = db.Column(db.ForeignKey('t_user.id'), index=True)
    status = db.Column(db.INTEGER)
    work_type = db.Column(db.String(32))
    t_user = relationship('User')
    t_user1 = relationship('User', secondary='t_sp')


class History(db.Model):
    __tablename__ = 't_history'

    id = db.Column(db.INTEGER, primary_key=True)
    pid = db.Column(db.ForeignKey('t_project.id'), index=True)
    info = db.Column(db.String(500))
    status = db.Column(db.INTEGER)
    uid = db.Column(db.ForeignKey('t_user.id'), index=True)

    t_project = relationship('Project')
    t_user = relationship('User')


t_t_sp = db.Table(
    't_sp', db.metadata,
    db.Column('pid', db.ForeignKey('t_project.id'), primary_key=True, nullable=False),
    db.Column('uid', db.ForeignKey('t_user.id'), primary_key=True, nullable=False, index=True)
)
