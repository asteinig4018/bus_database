from flask import Flask, render_template, jsonify, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
db.init_app(app)

@app.route("/")
def index():
    #routes = Route.query.all()
    route_and_bus = db.session.query(Route,Bus).filter(Route.bus_id == Bus.id).all()
    #print(str(temp_var.bus.company))
    return render_template("index.html", route_and_bus=route_and_bus)

    