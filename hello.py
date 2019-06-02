from flask import Flask, render_template, request
from models import db, Bus, Passenger

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bpgkosspwilapk:407d35d8781b7ca4dceed899e56a9ffa99c19bc07c93152c7240378ea1d667d1@ec2-54-221-198-156.compute-1.amazonaws.com:5432/dfn4cgu04vntbb'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html", about=True)


@app.route('/book')
def book():
    buses = Bus.query.all()
    return render_template('buses.html', buses=buses, about=False)


@app.route('/success', methods=['POST'])
def success():
    try:
        bus_id = int(request.form.get('selector_bus'))
        gender = int(request.form.get('gender'))
        age = request.form.get('age')
    except ValueError:
        return render_template('error.html', message='Bus ID failure!', about=False)

    user_bus = Bus.query.get(bus_id)
    name = request.form.get('name')
    if not name.isalpha():
        return render_template('error.html', message='Name is not correct!', about=False)

    if gender == 1:
        gen = 'M'
    else:
        gen = 'F'

    pid = db.session.query(db.func.max(Passenger.id)).scalar()
    user_bus.add_passenger(name, age, gen, pid+1)
    return render_template('success.html', user_bus=user_bus, name=name, age=age, gender=gen, about=False)


if __name__ == "__main__":
    app.run()