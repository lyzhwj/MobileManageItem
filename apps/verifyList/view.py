from flask import render_template
from apps.verifyList import verify

@verify.route('/verify/', methods=['GET'])
def verify_list():
    return render_template('verify/verifylistshow.html')