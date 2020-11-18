# Import dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setup database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station

# Setup Flask
app = Flask(__name__)

# Setup Flask routes
@app.route("/")
def home():
    print("Home page requested...")
    return(
        f"Available routes<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/stations<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Precipatation page requested...")
    session = Session(engine)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.prcp >= 0.00).\
    filter(Measurement.date >= '2016-08-23').\
    group_by(Measurement.date).all()

    session.close()

    return jsonify(precipitation_data)
@app.route("/api/v1.0/stations")
def stations():
    print("Stations page requested...")
    session = Session(engine)
    stations = session.query(Station.station, Measurement.tobs).\
    group_by(Station.station).\
    order_by(func.count(Station.station).desc()).all()

    session.close()
    
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    print("Tobs page requested...")
    session = Session(engine)
    highest_temp = session.query(Station.station, Measurement.date, Measurement.tobs).\
    filter(Station.station == 'USC00519281').\
    filter(Measurement.date >= '2016-08-23').all()

    session.close()

    return jsonify(highest_temp)


if __name__ == "__main__":
    app.run(debug=True)