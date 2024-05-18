from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes.user import user
from .routes.main import main


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(user)
    app.register_blueprint(main)

    db.init_app(app)
    migrate.init_app(app, db)

    return app