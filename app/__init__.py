from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes.user import user
from .routes.main import main


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user)
app.register_blueprint(main)