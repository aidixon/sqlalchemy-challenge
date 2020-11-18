# Import dependencies
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return(
        f"Available routes<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations"
    )

if __name__ == "__main__":
    app.run(debug=True)