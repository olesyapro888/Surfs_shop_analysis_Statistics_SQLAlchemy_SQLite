import datetime as dt
import numpy as np
import pandas as pd
# dependencies for SQLAlchemy
# Python SQL toolkit and Object Relational Mapper to query a SQLite database
import sqlalchemy
# Automatically generates mapped classes and relationships from a database schema
from sqlalchemy.ext.automap import automap_base
# the Session establishes all conversations with the database and 
# represents a “holding zone” for all the objects
from sqlalchemy.orm import Session
# Generic function invoked by using the func attribute
from sqlalchemy import create_engine, func

# dependencies for Flask
from flask import Flask, jsonify

# access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect the database into our classes
Base = automap_base()

# reflect the tables (reflect the schema from the tables to our code)
Base.prepare(engine, reflect=True)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session link from Python to our database
session = Session(engine)

# define our Flask app
app = Flask(__name__)

# define the welcome route 
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
      /n api/v1.0/precipitation 
      /n api/v1.0/stations
      /n api/v1.0/tobs
      /n api/v1.0/temp/start/end
    ''')

# create a new route, your code should be aligned to the left 
@app.route("/api/v1.0/precipitation")

def precipitation():
# calculates the date one year ago from the most recent date in the database
  prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
  #  a query to get the date and precipitation for the previous year.
  precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
  precip = {date: prcp for date, prcp in precipitation}
  return jsonify(precip)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)