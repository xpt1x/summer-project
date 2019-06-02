from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for

db = SQLAlchemy()


class Bus(db.Model):
    __tablename__ = "bus_data"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=True)

    def __init__(self, i, o, des, dur, p):
        self.id = i
        self.origin = o
        self.destination = des
        self.duration = dur
        self.price = p

    def addbus(self):
        db.session.add(self)
        db.session.commit()
      
    def add_passenger(self, name, age, gender, pid):
        p = Passenger(id=pid, name=name, age=age, gender=gender, bus_id=self.id)
        db.session.add(p)
        db.session.commit()


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    bus_id = db.Column(db.Integer, nullable=False)


class Panel(db.Model):
    __tablename__ = "panel"
    user = db.Column(db.String, primary_key=True, nullable=False)
    password = db.Column(db.String, nullable=False)
