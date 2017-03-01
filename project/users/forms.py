from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo

class UserForm(FlaskForm):
    username = StringField('Username', [Length(min=4, max=12), InputRequired()])
    email = StringField('Email', [Email(), InputRequired()])
    password = PasswordField('Password', [Length(min=6, max=16), InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', [Length(min=6, max=16)])
    first_name = StringField('First Name', [InputRequired()])
    last_name = StringField('Last Name', [InputRequired()])

class LoginForm(FlaskForm):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [Length(min=6)])
