from flask import Flask, render_template
from apps.user import user_bp

app = Flask(__name__)

app.register_blueprint(user_bp)


@app.route('/')
def hello_world():
    return render_template('base_index.html')
