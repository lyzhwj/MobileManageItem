from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

from apps import config



from apps.addproject import addproject
from apps.user import user_bp


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from apps.user import user_bp
from apps.workListView import wkl

app.register_blueprint(user_bp)

app.register_blueprint(wkl)

db = SQLAlchemy(app)

from apps.model import TUser

app.register_blueprint(addproject)



@app.route('/')
def hello_world():

    return render_template('base_index.html')



