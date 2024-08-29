from flask import *
from flask import Blueprint

import json, time

import dao.file.struct as struct
import dao.db.sdata as sdata

receive_bp = Blueprint("receive", __name__)


@receive_bp.route("/receive/<id>", methods=["POST"])
def receive(id: str):
    request_data = json.loads(request.data)
    data = {}
    if struct.needTimestamp(id):
        data["timestamp"] = int(time.time())
    keylist = struct.getSensorKey(id)
    for key in keylist:
        data[key[0]] = request_data[key[0]]
    if id in struct.getSensorList():
        sdata.writeData(id, data)
        return "OK"
    return abort(400)
