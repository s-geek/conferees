from app import app
from flask import render_template, request, redirect, url_for, flash, make_response, session
from datetime import datetime, time
from .models import Event, db
from .forms import EventForm, LoginForm
from sqlalchemy.sql.expression import func

@app.route('/')
def index():
    event_list = db.session.query(Event).order_by(-Event.date_start).all()
    cur = db.session.execute('SELECT DISTINCT year(date_start) as year_num FROM events order by year_num desc limit 12')
    year_list = cur.fetchall()
   # e = Event.query.filter(func.year(Event.date_start)=='2020').all()
    return render_template('index.html', event_list=event_list, year_list=year_list)


@app.route('/event/add', methods=['GET', 'POST'])
def event_add():
    form = EventForm()
    form.date_start.data = datetime.now()
    form.time_start.data = datetime.now().time()
    form.date_end.data = datetime.now()
    if form.validate_on_submit():
        name = form.name.data
        place = form.place.data
        date_start = form.date_start.data
        time_start = form.time_start.data
        date_end = form.date_end.data
        notes = form.notes.data
        rec_data = Event(name = name, place = place, date_start = date_start, time_start = time_start, date_end = date_end, notes = notes)
        db.session.add(rec_data)
        db.session.commit() 
        return redirect('/')
    return render_template('new_event.html', form=form)