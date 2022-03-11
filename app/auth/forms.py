from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo




class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')