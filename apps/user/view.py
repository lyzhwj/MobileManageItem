from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from apps import app
from apps.model import TProject, THistory
from apps.user import user_bp

'''
page: url传参
pid: url传参
status: url传参
uid: 通过session获取uid,进行是否已登录验证，可以写一个验证函数
'''

db = SQLAlchemy(app)


@user_bp.route('/login/')
def login_view():
    return render_template('login.html')


@user_bp.route('/register/')
def register_view():
    return render_template('register.html')


@user_bp.route('/login_out/')
def login_out_view():
    return render_template('login.html')
