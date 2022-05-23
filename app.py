# Dependencies
## from ntpath import join
from flask import Flask 

# Import Flask
from flask import Flask, jsonify, request, render_template

# Dependencies and Setup
import numpy as np
import datetime as dt

# Python SQL Toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.pool import StaticPool

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={"check_same_thread": False}, poolclass=StaticPool, echo=True)

# Automap
Base = automap_base()
# Reflect tables
Base.prepare(engine, reflect=True)

# Save references to tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create Session from Python to the db
session = Session(engine)

# Flask Setup
app = Flask(__name__)

# Credit for photo -- sean-oulashin-KMn4VEeEPR8-unsplash.jpg
# Native photo url "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.
# 1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=873&q=80"

# Flask Routes
# Home Route
@app.route("/")
def welcome():
    '''Homepage Hawaiian Vacation App'''
 # Get the most active station id 
    mostactive = session.query(Measurement.station, func.count(Measurement.station)).\
             group_by(Measurement.station).\
             order_by(func.count(Measurement.station).desc()).first()
    mostactivestation = mostactive[0]

    homehtml =  """<html>
<head>
    <title>Hawaii App</title>
    <style>
        h1 {{text-align: center;color: teal;}}
        h3 {{color: teal;}}
        li {{color: darkslategrey;}}
        li {{color: darkseagreen;}}
        a  {{color: darkslategrey;}}
        i  {{margin : 0; padding-top:0;}}
        button {{color: darkturquoise}}
    </style>
</head>
<body>
    <h1>Your Awesome Hawaii Trip - Weather App</h1>
    <img src="https://tinyurl.com/mryauj9z" alt="Hawaii Weather" align="right"/>
    <!--<img src="" alt="Hawaii Weather"/>-->

    <h3>Precipitation Analysis:</h3>
    <p>Will I need a raincoat?</p>
    <ul>
        <li><a href="/api/v1.0/precipitation">Precipitation</a></li>
    </ul>

    <h3>Station Analysis:</h3>
    <p> Where are we measuring this rain?</p>
    <ul>
        <li><a href="/api/v1.0/stations">Stations</a></li>
    </ul>

    <h3 style="margin-bottom:0;">Temperature Analysis:</h3>
    <i>Most active station: {mostactivestation}</i>
    <p>Do I need sweaters or shorts?</p>
    <ul>
        <li><a href="/api/v1.0/tobs">Most Active Station</a></li>
    </ul>

    <h3 style="margin-bottom:0;">Temperature Observations:</h3>
    <i>Minimum, Average and Maximum</i>
    <p>Temperatures for a year starting with entered date.</p>
    <form action = "/api/v1.0/start_day", method="post">
        <label for="startdate">Enter a start date:&nbsp;</label>
        <input type="date" name="startdate">
        <button type = "submit">Submit</button>
    </form>

    <p>Temperature Observations for date range:</p>
    <form action = "/api/v1.0/start_end", method="post">
        <label for="startdate">Enter a start date:&nbsp;</label>
        <input type="date" name="startdate">
        <br>
        <label for="enddate">Enter an end date:</label>
        <input type="date" name="enddate">
        <button type = "submit">Submit</button>
    </form>
    </ul>
</body>
</html>
""".format(mostactivestation=mostactivestation)
    return homehtml

# Precipitation Route
@app.route("/api/v1.0/precipitation")
def precipitation():
        '''Precipitation API Hawaiian Vacation App'''
        # Convert the Query Results to a Dictionary Using `date` as the Key and `prcp` as the Value
        # Get the latest datefrom the db
        last_point = session.query(func.max(Measurement.date)).first()
        # Convert list into single date    
        last_date = dt.datetime.strptime(last_point[0], "%Y-%m-%d").date()
        # Find start date for one year period
        OneYear = last_date - dt.timedelta(days=365)
        # Retrieve the Last 12 Months of Precipitation Data Selecting Only the `date` and `prcp` Values
        prcp_data = session.query(Measurement.date, Measurement.prcp).\
                filter(Measurement.date >= OneYear).\
                order_by(Measurement.date).all()
        # Convert List of Tuples Into a Dictionary
        prcp_data_list = dict(prcp_data)
        # Return JSON Representation of Dictionary
        return jsonify(prcp_data_list)

# Station Route
@app.route("/api/v1.0/stations")
def stations():
        '''List of all Stations API Hawaiian Vacation App'''
        # Return a JSON List of Stations From the Dataset
        stations_all = session.query(Station.station, Station.name).all()
        # Convert List of Tuples Into Normal List
        station_ret = dict(stations_all)
        # Return JSON List of Stations from the Dataset
        return jsonify(station_ret)
        #return station_list

# TOBs Route
@app.route("/api/v1.0/tobs")
def tobs():
        '''Temperature observations most active station API Hawaiian Vacation App'''
        # Get the most active station id 
        mostactive = session.query(Measurement.station, func.count(Measurement.station)).\
                group_by(Measurement.station).\
                order_by(func.count(Measurement.station).desc()).first()
        mostactivestation = mostactive[0]
        # Query for the Dates and Temperature Observations from a Year from the Last Data Point
        # Get the latest datefrom the db
        last_point = session.query(func.max(Measurement.date)).first()
        # Convert list into single date    
        last_date = dt.datetime.strptime(last_point[0], "%Y-%m-%d").date()
        # Find start date for one year period
        OneYear = last_date - dt.timedelta(days=365)
        # Retrieve the last 12 months of precipitation data 
        tobs_data = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.station == mostactivestation).\
                filter(Measurement.date >= OneYear).\
                order_by(Measurement.date).all()
        # Convert to dictionary
        tobs_data_ret = dict(tobs_data)
        # Return JSON List of Temperature Observations (tobs) for the Previous Year
        return jsonify(tobs_data_ret)

# Date Choice Route
@app.route("/api/v1.0/start_day", methods=["GET", "POST"])
def start_day():
    '''Temperature observations by user selected date station API Hawaiian Vacation App'''
    startd = request.form.get('startdate')
    if startd >= "1":
        startdd = dt.datetime.strptime(startd, "%Y-%m-%d").date()
        start_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= startdd).\
                group_by(Measurement.date).all()
        # Convert to a list
        # all_names = list(np.ravel(results)) # alternative
        start_day_ret = list(start_day)
        startdayJlist = [{"DT": dt, "tmin": tmin, "tavg": tavg, "tmax": tmax} for dt, tmin, tavg, tmax in start_day_ret]
        # Return JSON List of Min Temp, Avg Temp and Max Temp for a Given Start Range
        return jsonify(startdayJlist)
    else:
        # Return error if no date is entered - for entered date that is not in the dataset
        # an empty results is retuned
        return '<h2 style="color:red;">Please select a valid date.</h2>'
        #### return jsonify({"error": f"Please enter a valid dadte."}), 404

# Start-End Day Route
@app.route("/api/v1.0/start_end", methods=["GET", "POST"])
def start_end():
    '''Temperature observations by user selected dates station API Hawaiian Vacation App'''
    startd = request.form.get('startdate')
    endd = request.form.get('enddate')
    if startd >= "1" and endd >= startd:
        start = dt.datetime.strptime(startd, "%Y-%m-%d").date()
        end = dt.datetime.strptime(endd, "%Y-%m-%d").date()
        start_end_day = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start).\
                filter(Measurement.date <= end).\
                group_by(Measurement.date).all()
        # Convert List of Tuples to list
        se_ret = list(start_end_day)
        sedayJlist = [{"DT": dt, "tmin": tmin, "tavg": tavg, "tmax": tmax} for dt, tmin, tavg, tmax in se_ret]
        # Return JSON list of Min Temp, Avg Temp and Max Temp for a Given Start-End Range
        return jsonify(sedayJlist)
    elif endd < startd:
        # If end date entered is before startdate return before date message
        return '<h2 style="color:red;">Start date must be before end date.</h2>'
    else:
        # If start date not entered return valid date message
        return '<h2 style="color:red;">Please select a valid date.</h2>'

# Define behavoir for main
if __name__ == '__main__':
    app.run(debug=True)