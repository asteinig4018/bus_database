import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Route(db.Model):
    __tablename__ = "routes"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    bus_id = db.Column(db.Integer, db.ForeignKey("buses.id"), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    num_passengers = db.Column(db.Integer, nullable=False)
    seats_available = db.Column(db.Integer)
    passengers = db.relationship("Passenger", backref="route", lazy=True)




class Bus(db.Model):
    __tablename__ = "buses"
    id = db.Column(db.Integer, primary_key=True)
    seats = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String, nullable=False)



class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    route_id = db.Column(db.Integer, db.ForeignKey("routes.id"), nullable=False)