from datetime import datetime
from flask import Flask, render_template, request, redirect, session, url_for

from apps.user import user_bp, category_bp
from apps.model import User, db, Dictionary


@user_bp.route('/login/', methods=['POST', 'GET'])
def login_view():
    '''登录'''
    if request.method == 'GET':
        return render_template('login.html')
    else:
        uname = request.form.get('uname')
        user = User.query.filter_by(uname=uname).first()
        if user:
            password = request.form.get('pwd')
            if user.pwd == password:
                session['user'] = user.uname
                return redirect(url_for('user.index_view'))
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
        uname = request.form.get('uname')
        flag = User.query.filter_by(uname=uname).first()
        if not flag:
            pwd = request.form.get('pwd')
            user = User(uname=uname, pwd=pwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.login_view'))
        else:
            return render_template('register.html')


@category_bp.route('/index01/', methods=['POST', 'GET'])
def index_01_view():
    name = request.form.get('name')
    flag = Dictionary.query.filter_by(name=name).first()
    if not flag:
        pid = request.form.get('pid')
        type = request.form.get('types')
        if not all([pid, name, type]):
            return render_template('category_add.html', user=session['user'])
        dict = Dictionary(name=name, pid=pid,type=type)
        db.session.add(dict)
        db.session.commit()
        return render_template('category_add.html', user=session['user'])
    else:
        return render_template('category_add.html', user=session['user'])


@category_bp.route('/index02/', methods=['POST', 'GET'])
def index_02_view():
    if request.method == 'GET':
        categorys = Dictionary.query.filter(Dictionary.type == '项目类别').all()
        return render_template('category_list.html', categorys=categorys)


@user_bp.route('/index/')
def index_view():
    return render_template('index.html', user=session['user'])


@user_bp.route('/login/')
def login_out_view():
    '''退出'''
    return render_template('login.html')



@category_bp.route("/index02", methods=['POST'])
def dele_cate_view():
    cate_name = request.values.get("name")
    cate_del = Dictionary.query.filter_by(cate_name=cate_name).first()
    db.session.delete(cate_del)
    db.session.commit()
    return render_template('category_list.html')


