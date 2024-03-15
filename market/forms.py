from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo,Email,DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):
    # validate_username => name is given like this as FlaskForm understands in this way only we need to have validate keyword in function and after a underscore there should be the field name

    def validate_username(self, username_to_check):
        user= User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different user name')

    def validate_email_address(self, email_to_chack):
        email_address = User.query.filter_by(email_address=email_to_chack.data).first()
        if email_address:
            raise ValidationError('Account with this email already exists')


    username = StringField(label='User Name:' , validators=[Length(min=2,max=30),DataRequired()])
    email_address = StringField(label='Email Address:',validators=[Email() ,DataRequired()])
    password1 = PasswordField(label='Password:',validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username= StringField(label='User Name: ', validators=[Length(min=2,max=30),DataRequired()])
    password = PasswordField(label='Password: ',validators=[Length(min=6),DataRequired()])
    submit = SubmitField(label='Sign in')
