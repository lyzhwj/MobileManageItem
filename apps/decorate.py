import functools
from flask import session, redirect, url_for


def login_required(func):

    @functools.wraps(func)  # 修饰内层函数，防止当前装饰器去修改被装饰函数__name__的属性
    def inner(*args, **kwargs):
        user = session.get('user')
        if not user:
            return redirect(url_for('user.login_view'))
        else:
            return func(*args, **kwargs)

    return inner
