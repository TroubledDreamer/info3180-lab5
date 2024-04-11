# Add any form classes for Flask-WTF here called movieform

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileAllowed

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    poster = FileField('Poster', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!'), DataRequired()])