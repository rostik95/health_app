import os
import secrets
from pathlib import Path

from flask import current_app
from PIL import Image


def save_picture(path: str, picture: Image) -> str:
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = path + random_hex + f_ext
    picture_path= os.path.join(current_app.config['SERVER_PATH'], picture_fn)
    output_size = (256, 256)
    i = Image.open(picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    i.close()
    return picture_fn