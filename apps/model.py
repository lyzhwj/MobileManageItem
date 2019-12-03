# coding: utf-8
from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from apps import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class Dictory(db.Model):
    __tablename__ = 't_dict'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(32))
    pid = Column(INTEGER(11))


class User(db.Model):
    __tablename__ = 't_user'

    id = Column(INTEGER(11), primary_key=True)
    uname = Column(String(32))
    nick_name = Column(String(32))
    pwd = Column(String(32))
    rid = Column(INTEGER(2))
    is_used = Column(INTEGER(2))


class Project(db.Model):
    __tablename__ = 't_project'

    id = db.Column(INTEGER(11), primary_key=True)
    name = db.Column(String(32))
    catgory = db.Column(String(32))
    uid = db.Column(ForeignKey('t_user.id'), index=True)
    pre_ini_data = db.DateTime()
    pre_end_data = db.DateTime()
    rea_ini_data = db.DateTime()
    rea_end_data = db.DateTime()
    status = db.Column(INTEGER(11))
    total_account = db.Column(db.FLOAT)

    t_user = relationship('TUser')
    t_user1 = relationship('TUser', secondary='t_sp')


class History(db.Model):
    __tablename__ = 't_history'

    id = Column(INTEGER(11), primary_key=True)
    pid = Column(ForeignKey('t_project.id'), index=True)
    info = Column(String(500))
    staus = Column(INTEGER(11))
    uid = Column(ForeignKey('t_user.id'), index=True)

    t_project = relationship('TProject')
    t_user = relationship('TUser')


t_t_sp = Table(
    't_sp', db.metadata,
    Column('pid', ForeignKey('t_project.id'), primary_key=True, nullable=False),
    Column('uid', ForeignKey('t_user.id'), primary_key=True, nullable=False, index=True)
)
