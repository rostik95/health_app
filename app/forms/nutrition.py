from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import FileField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class AddFoodForm(FlaskForm):
    name = StringField(
        label="Название блюда", validators=[DataRequired("Введите название блюда")]
    )
    photo = FileField(
        label="Фото еды",
        validators=[
            FileAllowed(
                ["jpg", "jpeg", "png"], "Загрузите фото в формате *.jpg, *jpeg или *png"
            ),
            DataRequired("Добавьте фотографию"),
        ],
    )
    kcal = IntegerField(
        label="Килокалории",
        validators=[
            DataRequired("Введите килокалории"),
            NumberRange(min=0, message="Количество калорий не может быть меньше нуля"),
        ],
    )
    proteins = IntegerField(
        label="Белки",
        validators=[
            DataRequired("Введите белки"),
            NumberRange(min=0, message="Количество белков не может быть меньше нуля"),
        ],
    )
    fats = IntegerField(
        label="Жиры",
        validators=[
            DataRequired("Введите жиры"),
            NumberRange(min=0, message="Количество жиров не может быть меньше нуля"),
        ],
    )
    carbs = IntegerField(
        label="Углеводы",
        validators=[
            DataRequired("Введите углеводы"),
            NumberRange(
                min=0, message="Количество углеводов не может быть меньше нуля"
            ),
        ],
    )
    submit = SubmitField(label="Добавить")


class IngestionForm(FlaskForm):
    grams = IntegerField(
        label="Съедено грамм",
        validators=[
            DataRequired("Введите количество съеденных грамм еды"),
            NumberRange(min=0, message="Вес съеденной еды не может быть меньше нуля"),
        ],
    )
    submit = SubmitField(label="Добавить")
