from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, NumberRange
from app import db
from .custom import MyFloatField
from ..models.user import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired('Поле не должно быть пустым')])
    password = PasswordField('Пароль', validators=[DataRequired('Поле не должно быть пустым')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class BodyParametersMixin:
    height = IntegerField(
        label='Введите рост (см)',
        validators=[
            DataRequired('Поле роста не должно быть пустым'),
            NumberRange(min=0, message='Введите число не меньше нуля')
                ]
            )
    weight = MyFloatField(
        label='Введите вес (кг)',
        validators=[
            DataRequired('Поле веса не должно быть пустым'),
            NumberRange(min=0, message='Введите число не меньше нуля')
                ]
            )

class ChangeBodyParametersForm(FlaskForm, BodyParametersMixin):
    submit = SubmitField(label='Изменить')


class RegistrationForm(FlaskForm, BodyParametersMixin):
    username = StringField(label='Имя пользователя', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired('Поле не должно быть пустым'), Email('Введите корректный email')])
    password = PasswordField(label='Пароль', validators=[DataRequired('Поле не должно быть пустым')])
    password2 = PasswordField(label='Повторите пароль', validators=[DataRequired('Поле не должно быть пустым'), EqualTo('password', 'Пароли не совпадают')])
    submit = SubmitField(label='Зарегистрироваться')

    def validate_username(self, username):
        user = db.session.query(User).filter(User.username == username.data).first()
        if user is not None:
            raise ValidationError('Данное имя пользователя уже зарегистрировано')
        
    def validate_email(self, email):
        user = db.session.query(User).filter(User.email == email.data).first()
        if user is not None:
            raise ValidationError('Данный email адрес уже зарегистрирован')
