import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def import_buses():
    f = open("sample_data/sample_buses.csv")
    reader = csv.reader(f)
    for id, company, seats in reader:
        bus = Bus(id=id, seats=seats, company=company)
        db.session.add(bus)
        print(f"Added bus {id} of {company} with {seats} seats.")
    db.session.commit()

def import_routes():
    f = open("sample_data/sample_routes.csv")
    reader = csv.reader(f)
    for origin, destination, bus_id, duration, num_passengers in reader:
        route = Route(origin=origin, destination=destination, bus_id=bus_id, duration=duration, num_passengers=num_passengers)
        db.session.add(route)
        print(f"Added route from {origin} to {destination}.")
    db.session.commit()

def main():
    import_buses()
    import_routes()

if __name__=="__main__":
    with app.app_context():
        main()

