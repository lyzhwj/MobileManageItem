from flask import Flask, render_template
from apps.user import user_bp


@user_bp.route('/login/')
def login_view():
    return render_template('login.html')


@user_bp.route('/register/')
def register_view():
    return render_template('register.html')


@user_bp.route('/login_out/')
def login_out_view():
    return render_template('login.html')
