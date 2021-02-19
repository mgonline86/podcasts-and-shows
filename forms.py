from datetime import datetime
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, AnyOf, URL, Regexp
from wtforms.widgets.html5 import NumberInput


class ShowForm(Form):
    show_name = StringField(
        'show_name', validators=[DataRequired()]
    )
    host_name = StringField(
        'host_name', validators=[DataRequired()]
    )
    period = StringField(
        'period', validators=[DataRequired(), ]
    )
    episodes = IntegerField(
        'episodes', validators=[DataRequired(), Regexp('^[-+]?[0-9]+$', message="Username must contain only numbers")], widget=NumberInput())
    about = TextAreaField(
        'about', validators=[DataRequired()]
    )
    image_link = StringField(
        'image_link'
    )
