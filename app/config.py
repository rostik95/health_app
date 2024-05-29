from dotenv import load_dotenv
import os
from pathlib import Path


load_dotenv()


USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
HOST = os.environ.get("POSTGRES_HOST")
PORT = os.environ.get("POSTGRES_PORT")
DB = os.environ.get("POSTGRES_DB")

class Config:
    APPNAME = 'app'
    ROOT = os.path.abspath(APPNAME)
    MEDIA_PATH = 'static/media/'
    SERVER_PATH = os.path.join(ROOT, MEDIA_PATH)

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = True