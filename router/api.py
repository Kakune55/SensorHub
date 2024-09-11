from flask import *
from flask import Blueprint

import services.sensorlist as sensorlist

api_bp = Blueprint("api", __name__)


@api_bp.route("/api/sensorlist")
def sensorList():
    return jsonify(sensorlist.getSensorList())


@api_bp.route("/api/sensor/<id>/<num>")
def sensorNewData(id, num):
    zoom = request.args.get("zoom", 1, type=int)
    if zoom >= 1:
        return jsonify(sensorlist.getSensorNewData(id, int(num), zoom=zoom))
    else:
        return abort(400)
