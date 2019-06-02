from flask import Flask, render_template, request
from models import db, Passenger, Panel, Bus

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
    return render_template('buses.html', buses=buses)


@app.route('/success', methods=['POST'])
def success():
    try:
        bus_id = int(request.form.get('selector_bus'))
        gender = int(request.form.get('gender'))
        age = request.form.get('age')
    except ValueError:
        return render_template('error.html', message='Bus ID failure!')

    user_bus = Bus.query.get(bus_id)
    name = request.form.get('name')
    if not name.isalpha():
        return render_template('error.html', message='Name is not correct!')

    if gender == 1:
        gen = 'M'
    elif gender == 2:
        gen = 'F'
    else:
        gen = 'O'

    pid = db.session.query(db.func.max(Passenger.id)).scalar()
    if pid is None:
        pid = 0
    user_bus.add_passenger(name, age, gen, pid+1)
    return render_template('success.html', user_bus=user_bus, name=name, age=age, gender=gen)


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/panel', methods=['POST'])
def panel():
    admin = Panel.query.first()   # Only 1 admin
    userName = request.form.get('adminName')
    userPass = request.form.get('adminPass')

    if admin.user == userName and admin.password == userPass:
        return render_template('panel.html')
    else:
        return render_template('error.html', message='No access!')


@app.route('/pass', methods=['POST'])
def list_passengers():
    passengers = Passenger.query.all()
    return render_template('pass.html', passes=passengers)


@app.route('/addb', methods=['POST'])
def addb():
    return render_template('form_addb.html')


@app.route('/add_busdata', methods=['POST'])
def add_busdata():
    id = request.form.get('add_id')
    origin = request.form.get('add_ori')
    destination = request.form.get('add_dest')
    duration = request.form.get('add_duration')
    price = request.form.get('add_price')
    form_bus = Bus(id, origin, destination, duration, price)
    form_bus.addbus()
    return render_template('form_addb.html', success=True)


if __name__ == "__main__":
    app.run()
