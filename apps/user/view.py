from datetime import datetime
from flask import render_template, request, redirect, session, url_for
from apps.user import user_bp, category_bp
from apps.model import User, db


@user_bp.route('/login/', methods=['POST', 'GET'])
def login_view():
    '''登录'''
    if request.method == 'GET':
        return render_template('login.html')
    else:
        uname = request.values.get('uname')
        user = User.query.filter_by(uname=uname).first()
        if user:
            password = request.values.get('password')
            if user.password == password:
                session['user'] = user.name
                return render_template('index.html')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')


@user_bp.route('/register/', methods=['POST', 'GET'])
def register_view():
    '''注册'''
    if request.method == 'GET':
        return render_template('register.html')
    else:
        uname = request.values.get('uname')
        user = User.query.filter_by(uname=uname).first()
        if not user:
            password = request.values.get('password')
            user = User(name=uname, password=password, regis_date=datetime.now)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login_view'))
        else:
            return render_template('register.html')


@category_bp.route('/index01/')
def index_01_view():
    return render_template('category_add.html')


@category_bp.route('/index02/')
def index_02_view():
    return render_template('category_list.html')



@user_bp.route('/login/')
def login_out_view():
    '''退出'''
    return render_template('login.html')
