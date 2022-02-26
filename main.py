from flask import Flask
import config
from utils import Logger
from threading import Thread
import Routes

logger = Logger.logger
Logger.logging_start()
app = Flask(__name__)

for route in Routes.routes:
    app.add_url_rule(route['route'], route['name'], route['function'], methods=route['methods'])
    logger.info("Created route: " + route['name'] + " on works: http://" + config.SERVER_HOST + ":" + str(config.SERVER_PORT) + str(route['route']) + " works with methods: " +str(route['methods']))
try:
    logger.info("Webserver successfully created. Connect with http://%s:%s" % (config.SERVER_HOST, config.SERVER_PORT))
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
except Exception as e:
    logger.critical("Couldn't created webserver.")
    logger.error("ERROR", e)