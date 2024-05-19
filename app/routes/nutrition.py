from flask import Blueprint, render_template


nutrition_bp = Blueprint('nutrition_bp', __name__)

@nutrition_bp.route('/')
def index():
    return render_template('nutrition/index.html')