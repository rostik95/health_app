from flask import Blueprint, redirect, render_template, url_for, abort
from flask_login import current_user, login_required
from sqlalchemy import select, func
from datetime import datetime

from ..models.user import User

from ..extensions import db
from ..functions import save_picture
from ..models.nutrition import Food, Ingestion
from ..forms.nutrition import AddFoodForm, IngestionForm


nutrition_bp = Blueprint('nutrition_bp', __name__)

@nutrition_bp.route('/')
def index():
    foods = Food.query.all()
    return render_template('nutrition/index.html', foods=foods)


@nutrition_bp.route('/add_food', methods=['GET', 'POST'])
def add_food():
    form = AddFoodForm()
    if form.validate_on_submit():
        food = Food(
            photo=save_picture('nutrition/', form.photo.data),
            name=form.name.data,
            kcal=form.kcal.data,
            proteins=form.proteins.data,
            fats=form.fats.data,
            carbs=form.carbs.data
        )
        db.session.add(food)
        db.session.commit()
        return redirect(url_for('nutrition_bp.index'))
    return render_template('nutrition/add_food.html', form=form)


@nutrition_bp.route('/ingestion/<food_id>', methods=['GET', 'POST'])
@login_required
def ingestion(food_id: int):
    form = IngestionForm()
    stmt = select(Food).where(Food.id == food_id)
    food: Food = db.session.scalar(stmt)
    if not food:
        abort(404)
    stmt = select(User).where(User.username == current_user.username)
    user: User = db.session.scalar(stmt)
    if form.validate_on_submit():
        print(food.kcal)
        print(form.grams.data)
        print(food.kcal / 100 * form.grams.data)
        ingestion = Ingestion(grams=form.grams.data, user=user, food=food)
        db.session.add(ingestion)
        db.session.commit()
        return redirect(url_for('nutrition_bp.index'))
    return render_template('nutrition/ingestion.html', form=form)

@nutrition_bp.route('/kcal_received')
@login_required
def kcal_received():
    stmt = (select(Ingestion).filter(func.date(Ingestion.timestamp) == datetime.now().date())
            .filter(Ingestion.user_id == current_user.id))
    ingestions: list[Ingestion] = db.session.scalars(stmt).all()
    kcal_all = round(sum(map(lambda x: x.food.kcal / 100 * x.grams, ingestions)), 2)
    return render_template('nutrition/kcal_received.html', ingestions=ingestions, kcal_all=kcal_all)