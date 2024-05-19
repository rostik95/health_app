from flask import Blueprint, redirect, render_template, url_for, flash
from ..models.user import User
from flask_login import current_user, login_required, login_user, logout_user
from ..forms.user import LoginForm, RegistrationForm
from ..extensions import db


user_bp = Blueprint('user_bp', __name__, url_prefix='/user')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('nutrition_bp.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(User).filter(User.username == form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Введите другие имя пользователя или пароль")
            return redirect(url_for('user_bp.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('nutrition_bp.index'))
    return render_template('user/login.html', form=form)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('nutrition_bp.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы зарегистрировались!')
        return redirect(url_for('user_bp.login'))
    return render_template('user/register.html', form=form)


@user_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('nutrition_bp.index'))