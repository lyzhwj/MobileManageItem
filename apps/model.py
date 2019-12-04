# coding: utf-8
from datetime import datetime

from apps import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Dictionary(db.Model):
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
    pname = db.Column(db.String(32))
    catgory = db.Column(db.String(33))
    uid = db.Column(db.ForeignKey('t_user.id'), index=True)
    pre_ini_date = db.Column(db.DateTime)  # 预计启动时间
    rea_ini_date = db.Column(db.DateTime)  # 实际启动时间
    pre_end_date = db.Column(db.DateTime)  # 预计结束时间
    rea_end_date = db.Column(db.DateTime)  # 实际结束时间
    update_date = db.Column(db.DateTime, default=datetime.now())  # update时间
    province = db.Column(db.String(32))
    tel = db.Column(db.String(32))
    total_account = db.Column(db.FLOAT)
    info = db.Column(db.String(256))
    status = db.Column(db.Integer)

    user = db.relationship('User')


class History(db.Model):
    __tablename__ = 't_history'

    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.ForeignKey('t_project.id'), index=True)
    info = db.Column(db.String(500))
    staus = db.Column(db.Integer)
    opa_time = db.Column(db.DateTime, default=datetime.now())  # 操作时间
    uid = db.Column(db.ForeignKey('t_user.id'), index=True)

    t_project = db.relationship('Project')
    t_user = db.relationship('User')


class Province(db.Model):
    __tablename__ = 't_province'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))


class Officer(db.Model):
    __tablename__ = 't_officer'
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.ForeignKey('t_project.id'))
    uid = db.Column(db.ForeignKey('t_user.id'))




t_t_sp = db.Table(
    't_sp', db.metadata,
    db.Column('pid', db.ForeignKey('t_project.id'),
              primary_key=True, nullable=False),
    db.Column('uid', db.ForeignKey('t_user.id'),
              primary_key=True, nullable=False, index=True)
)
