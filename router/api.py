from flask import *
from flask import Blueprint

import services.sensorlist as sensorlist

api_bp = Blueprint("api", __name__)

@api_bp.route("/api/sensorlist")
def sensorList():
    return jsonify(sensorlist.getSensorList())


@api_bp.route("/api/sensor/<id>/<num>")
def sensorNewData(id,num):
    return jsonify(sensorlist.getSensorNewData(id,int(num)))
