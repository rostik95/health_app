from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app import db
from ..models.user import User


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired('Поле не должно быть пустым')])
    password = PasswordField('Пароль', validators=[DataRequired('Поле не должно быть пустым')])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField(label='Имя пользователя', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
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