from flask import *
import logging, os

import appconfig
import dao.db.sdata
import dao.file.struct

from router.receive import receive_bp
from router.page import page_bp
from router.api import api_bp


logging.basicConfig(level=logging.INFO)
# 读取配置文件
conf = appconfig.conf()
logging.info("Config Loaded")

app = Flask(__name__)

app.register_blueprint(receive_bp)
app.register_blueprint(page_bp)
app.register_blueprint(api_bp)


def init():
    if not os.path.exists("./data"):
        logging.info("Data folder not found, creating...")
        os.mkdir("./data")
    if dao.file.struct.init():
        logging.info("Struct file initialized")
    dao.db.sdata.init()


if __name__ == "__main__":
    logging.info("Server Initialized")
    init()
    logging.info("Server Started")
    app.run(
        debug=conf.getboolean("server", "debug"),
        host=conf.get("server", "host"),
        port=conf.get("server", "port"),
        threaded=conf.getboolean("server", "threaded"),
    )
