# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from apps import app

db = SQLAlchemy(app)
Base = declarative_base()
metadata = Base.metadata


class TDict(db.Model):
    __tablename__ = 't_dict'

    name = db.Column(String(32), primary_key=True)
    pid = db.Column(INTEGER(11), primary_key=True)


class TUser(db.Model):
    __tablename__ = 't_user'

    id = db.Column(INTEGER(11), primary_key=True)
    uname = db.Column(String(32))
    nick_name = db.Column(String(32))
    pwd = db.Column(String(32))
    rid = db.Column(INTEGER(2))
    is_used = db.Column(INTEGER(2))


class TProject(db.Model):
    __tablename__ = 't_project'

    id = db.Column(INTEGER(11), primary_key=True)
    name = db.Column(String(32))
    info = db.Column(String(32))
    uid = db.Column(ForeignKey('t_user.id'), index=True)
    status = db.Column(INTEGER(11))
    work_type = db.Column(String(32))
    t_user = relationship('TUser')
    t_user1 = relationship('TUser', secondary='t_sp')


class THistory(db.Model):
    __tablename__ = 't_history'

    id = db.Column(INTEGER(11), primary_key=True)
    pid = db.Column(ForeignKey('t_project.id'), index=True)
    info = db.Column(String(500))
    status = db.Column(INTEGER(11))
    uid = db.Column(ForeignKey('t_user.id'), index=True)

    t_project = relationship('TProject')
    t_user = relationship('TUser')


class T_t_sp(db.Model):
    __tablename__ = 't_sp'
    pid = db.Column(ForeignKey('t_project.id'), primary_key=True, nullable=False)
    uid = db.Column(ForeignKey('t_user.id'), primary_key=True, nullable=False, index=True)

    t_project = relationship('TProject')
    t_user = relationship('TUser')

# t_t_sp = Table(
#     't_sp', metadata,
#     Column('pid', ForeignKey('t_project.id'), primary_key=True, nullable=False),
#     Column('uid', ForeignKey('t_user.id'), primary_key=True, nullable=False, index=True)
# )
