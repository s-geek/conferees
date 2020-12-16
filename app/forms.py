from flask_wtf import FlaskForm
from wtforms import Form, ValidationError
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, DateField, TimeField
from wtforms.validators import DataRequired, Email
from wtforms.widgets import *
from wtforms.widgets.html5 import *


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Войти")


class EventForm(FlaskForm):
    name = TextAreaField("Наименование события", render_kw={"rows": 4, "cols": 100}, validators=[DataRequired()])
    place = TextAreaField("Место проведения", render_kw={"rows": 4, "cols": 100}, validators=[DataRequired()])
    date_start = DateField("Дата начала", validators=[DataRequired()], widget=DateInput())
    time_start = TimeField("Время начала", validators=[DataRequired()], widget=TimeInput())
    date_end = DateField("Дата окончания", validators=[DataRequired()], widget=DateInput())
    notes = TextAreaField("Примечание", render_kw={"rows": 4, "cols": 100})
    #submit = SubmitField("Сохранить", widget=SubmitInput())