from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Bus(db.Model):
    __tablename__ = "bus_data"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=True)

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
