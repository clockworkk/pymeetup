from app import db
import datetime
import date
import time

meetups = db.Table('meetups', 
    db.Column('meetup_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)
    events = db.relationship('Meetup', secondary=tags, backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username, email, first_name, last_name):
        self.username = username
	self.email = email
	self.first_name = first_name
	self.last_name = last_name
	self.events = events

    def __repr__(self):
        return '<User %r>' % (self.username)

class Meetup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(120), index=True)
    creator = db.Column(db.String(64), index=True)
    event_date = db.Column(db.DateTime(), index=True)
    time = db.Column(db.String(8), index=True)
    location = db.Column(db.String(120), index=True)

    def __init(self, event_name, creator, event_date, time, location):
        self.event_name = event_name
	self.creator = creator
	self.event_date = event_date
        self.time = time
	self.location = location

    def __repr__(self):
        return '<Meetup %r %r %r %r %r>' % (self.event_name, self.creator, self.event_date, self.time, self.location)

