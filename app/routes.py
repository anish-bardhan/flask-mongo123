import os
from app import app
from flask import render_template, request, redirect

# the purpose of this application is to allow a user to upload information about upcoming events.

username = "benlee"

events = [
        {"event":"First Day of Classes", "date":"2019-08-21"},
        {"event":"Winter Break", "date":"2019-12-20"},
        {"event":"Finals Begin", "date":"2019-12-01"},
        {"event":"Summer Vacation", "date":"2019-06-14"}
    ]

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'test'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:MeUIrelr55kOTR8b@cluster0-2x8f2.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)


# INDEX

#sets the homepage
@app.route('/')
@app.route('/index', methods= ['GET','POST'])

def index():
    #
    for_display = {}
    information = mongo.db.events
    queries = list(information.find({}))
    print(queries)
    # prevent error before info is added
    if dict(request.form):
        # retrieve data from form
        added_data = dict(request.form)
        # find name
        event_name = added_data["event_name"]
        # find date
        date =  added_data["date"]
        # find attendance
        attending = added_data["attending"]
        event = mongo.db.events
        # send all info
        event.insert({"name":event_name, "date": date, "attending": attending})
    return render_template('index.html', queries = queries)


# CONNECT TO DB, ADD DATA

#creates a page for the form
@app.route('/input', methods= ['GET',"POST"])
def input():
    return render_template('input.html')


@app.route('/add')
def add():
    # connect to the database
    test = mongo.db.test
    # insert new data
    test.insert({'name': 'last day of school'})
    # return a message to the user
    return "added data to database"
