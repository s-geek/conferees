from app import db
from datetime import datetime, time
#from flask_login import (LoginManager, UserMixin, login_required, login_user, current_user, logout_user)
#from werkzeug.security import generate_password_hash, check_password_hash

class Event(db.Model):
    __tablename__ = 'events'
    __table_args__ = (
        db.UniqueConstraint('name', 'place', 'date_start', name='unique_event'),
    )
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    place = db.Column(db.String(255), nullable=False, unique=False)
    date_start = db.Column(db.DateTime(), default=datetime.utcnow)
    time_start = db.Column(db.Time(), nullable=False)
    date_end = db.Column(db.DateTime(), default=datetime.utcnow)
    notes = db.Column(db.String(1000), nullable=True, unique=False, default='')
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)    

    UniqueConstraint('col2', 'col3', name='uix_1')

    def __repr__(self):
        return "<{}:{}:{}>".format(self.id, self.date_start, self.name)
