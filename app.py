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
        f"/api/v1.0/stations"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Precipatation page")
    session = Session(engine)
    precipitation_data = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.prcp >= 0.00).\
    filter(Measurement.date >= '2016-08-23').\
    group_by(Measurement.date).all()

    session.close()




if __name__ == "__main__":
    app.run(debug=True)