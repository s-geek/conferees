from flask_wtf import FlaskForm
from wtforms import Form, ValidationError
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, DateField, TimeField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.widgets import *
from wtforms.widgets.html5 import *
from datetime import datetime, time
from .models import Event, db

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
    password = StringField("Password", validators=[InputRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Войти")


class EventForm(FlaskForm):
    name = TextAreaField("Наименование события", render_kw={"rows": 4, "cols": 100}, validators=[InputRequired()])
    place = TextAreaField("Место проведения", render_kw={"rows": 4, "cols": 100}, validators=[InputRequired()])
    date_start = DateField("Дата начала", validators=[InputRequired("Введите дату начала события.")], widget=DateInput(), default=datetime.now())
    time_start = TimeField("Время начала", validators=[InputRequired("Введите время начала события.")], widget=TimeInput())
    date_end = DateField("Дата окончания", validators=[InputRequired("Введите дату окончания события.")], widget=DateInput(), default=datetime.now())
    notes = TextAreaField("Примечание", render_kw={"rows": 4, "cols": 100})

    def validate_name(form, field):
        if len(field.data) < 3:
            raise ValidationError('Наименование события должно быть заполнено и быть длинной не менее 3-х символов.')

    def validate_place(form, field):
        if len(field.data) < 3:
            raise ValidationError('Место проведения события должно быть заполнено и быть длинной не менее 3-х символов.')    

    def validate_date_start(form, field):
        if not(field.data):
            raise ValidationError('Дата начала события должна быть заполнена.')
    
    def validate_time_start(form, field):
        if not(field.data):
            raise ValidationError('Время проведения события должно быть заполнено.')
    
    def validate_date_end(form, field):
        if not(field.data):
            raise ValidationError('Дата окончания события должна быть заполнена.')

    def validate(self):
        if not super(EventForm, self).validate():
            return False

        if Event.query.filter_by(name=self.name.data, place=self.place.data, date_start=self.date_start.data).first():
            self.name.errors.append('Данное событие уже существует для указанной даты и места проведения.')
            return False

        if self.date_start.data > self.date_end.data:
            self.date_end.errors.append('Дата окончания события не может быть раньше даты начала события.')
            return False
        return True
