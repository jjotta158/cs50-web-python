from flask import Flask, render_template, request
from flask_orm import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/airport"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route('/')
def index():
    flight = Flight()
    flights = flight.query.all()
    return render_template("allFlights.html", flights=flights)


@app.route('/flights')
def flights():
    flight = Flight()
    flights = flight.query.all()
    return render_template("allFlights.html", flights=flights)


@app.route('/addFlightForm')
def addFlightForm():
    return render_template("addFlightForm.html")


@app.route('/addFlight', methods=["POST"])
def addFlight():
    origin = request.form.get('origin')
    destination = request.form.get('destination')
    duration = request.form.get('duration')
    flight = Flight(origin=origin, destination=destination, duration=duration)
    db.session.add(flight)
    db.session.commit()
    return render_template("addFlightForm.html")


@app.route('/flightDetails/<id_flight>/')
def ListFlightDetails(id_flight):
    fly = Flight()
    flight = fly.query.filter_by(id=id_flight).all()
    passenger = Passenger()
    passengers = passenger.query.filter_by(flight_id=id_flight).all()

    return render_template("flightDetails.html", flights=flight, passengers=passengers)
