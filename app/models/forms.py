from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms_validators import AlphaNumeric

class LoginForm(FlaskForm):
    username = StringField('username', [
        validators.Length(min=4, max=12, message='O usuário deve conter 4 a 12 caracteres'),
        AlphaNumeric('O usuário deve conter apenas números e letras')
    ])
    password = StringField('password', [
        validators.Length(min=4, max=10, message='A senha deve conter 4 a 12 caracteres'),
        AlphaNumeric('A senha deve conter apenas números e letras')
    ])