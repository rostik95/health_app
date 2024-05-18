from flask import Blueprint, render_template
from ..models.user import User


user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/login')
def login():
    return render_template('user/login.html')