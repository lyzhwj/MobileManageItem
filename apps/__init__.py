from apps import config
from flask import Flask, render_template, redirect

app = Flask(__name__)
app.config.from_object(config)

app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from apps.user import user_bp, category_bp
app.register_blueprint(user_bp)
app.register_blueprint(category_bp)


from apps.workListView import wkl
app.register_blueprint(wkl)

from apps.addproject import addproject
app.register_blueprint(addproject)


@app.route('/')
def hello_world():
    return render_template('index.html')
