from flask import *
from flask import Blueprint

import dao.file.struct

page_bp = Blueprint("page", __name__)


@page_bp.route("/")
def index():
    return render_template("index.html")


@page_bp.route("/chart/<id>")
def watch(id):
    if not dao.file.struct.haveSensor(id):
        return render_template("404.html")
    else:
        return render_template("chart.html", id=id)
