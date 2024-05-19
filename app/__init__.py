from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager
from .config import Config
from .extensions import db, migrate, login
from .routes.user import user_bp
from .routes.nutrition import nutrition_bp
from .models.user import User


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user_bp)
    app.register_blueprint(nutrition_bp)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    # login.login_view = 'user_bp.login'
    admin = Admin(app, name='health_app', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))

    return app


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))