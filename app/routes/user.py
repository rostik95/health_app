from typing import Iterable
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from flask import Blueprint, Response, redirect, request, render_template, template_rendered, url_for, flash
from ..models.user import User, Weight
from flask_login import current_user, login_required, login_user, logout_user
from ..forms.user import LoginForm, RegistrationForm, ChangeBodyParametersForm
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
        user = User(username=form.username.data, email=form.email.data, height_in_cm=form.height.data)
        user.set_password(form.password.data)
        user.add_weight(form.weight.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы зарегистрировались!')
        return redirect(url_for('user_bp.login'))
    return render_template('user/register.html', form=form)


@user_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('nutrition_bp.index'))


@user_bp.route('/about_me/<username>', methods=['GET', 'POST'])
@login_required
def about_me(username: str) -> Response:
    if current_user.username != username:
        return redirect(url_for('user_bp.about_me', username=current_user.username))
    stmt = select(User).where(User.username == username)
    user: User = db.session.scalar(stmt)
    stmt2 = select(Weight).where(Weight.user_id == user.id).order_by(Weight.timestamp.desc())
    weights: Iterable[Weight] = db.session.scalars(stmt2).all()
    BMI = round(weights[0].value_in_kg / ((user.height_in_cm / 100)**2), 2)
    return render_template('user/about_me.html', user=user, weights=weights, BMI=BMI)


@user_bp.route('/update_me/<username>', methods=['GET', 'POST'])
@login_required
def update_me(username: str) -> Response:
    if current_user.username != username:
        return redirect(url_for('user_bp.update_me', username=current_user.username))
    form = ChangeBodyParametersForm()
    stmt = select(User).where(User.username == username)
    user: User = db.session.scalar(stmt)
    if form.validate_on_submit():
        print(form.height.data)
        print(form.weight.data)
        user.height_in_cm = form.height.data
        user.add_weight(form.weight.data)
        db.session.commit()
        return redirect(url_for('user_bp.about_me', username=username))
    elif request.method == 'GET':
        stmt2 = select(Weight).where(Weight.user_id == user.id).order_by(Weight.timestamp.desc())
        weight: Iterable[Weight] = db.session.scalars(stmt2).first()
        form.height.data = user.height_in_cm
        form.weight.data = weight.value_in_kg
    return render_template('user/update_me.html', form=form)