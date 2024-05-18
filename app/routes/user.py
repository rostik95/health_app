from flask import Blueprint, render_template


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login')
def login():
    return render_template('user/login.html')