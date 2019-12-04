from flask import Flask, render_template, redirect
from apps import config

app = Flask(__name__)
app.config.from_object(config)

from apps.user import user_bp, category_bp

app.register_blueprint(user_bp)
app.register_blueprint(category_bp)
app.config['SECRET_KEY'] = '123'

@app.route('/')
def hello_world():
    # return render_template('login.html')
    return redirect('/login/')

