from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from apps import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from apps.user import user_bp
from apps.workListView import wkl

app.register_blueprint(user_bp)
app.register_blueprint(wkl)

db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return render_template('base_index.html')
