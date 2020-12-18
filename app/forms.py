from flask_wtf import FlaskForm
from wtforms import Form, ValidationError
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, DateField, TimeField
from wtforms.validators import InputRequired
from wtforms.widgets import *
from wtforms.widgets.html5 import *
from datetime import datetime, time

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = StringField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Войти")


class EventForm(FlaskForm):
    name = TextAreaField("Наименование события", render_kw={"rows": 4, "cols": 100}, validators=[InputRequired()])
    place = TextAreaField("Место проведения", render_kw={"rows": 4, "cols": 100}, validators=[InputRequired()])
    date_start = DateField("Дата начала", validators=[InputRequired(message="Введите дату начала события")], widget=DateInput(), default=datetime.now())
    time_start = TimeField("Время начала", validators=[InputRequired(message="Введите время начала события")], widget=TimeInput())
    date_end = DateField("Дата окончания", validators=[InputRequired(message="Введите дату окончания события")], widget=DateInput(), default=datetime.now())
    notes = TextAreaField("Примечание", render_kw={"rows": 4, "cols": 100})
    #submit = SubmitField("Сохранить", widget=SubmitInput())

    def validate_name(form, field):
        if not(len(field.data) > 0):
            raise ValidationError('Наименование события должно быть заполнено')