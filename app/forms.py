from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators
from wtforms.validators import DataRequired, Email

class MyForm(FlaskForm):
    fullname = TextField('Full Name', validators=[DataRequired()])
    contact = TextField('Contact Number', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    description = TextAreaField('Description', validators=[DataRequired()])
   
    