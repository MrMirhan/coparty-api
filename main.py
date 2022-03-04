from flask import Flask, request, session
from flask_session import Session
import config
from utils import Logger, Returns, Telegram
import Routes
import shutil, os, requests

logger = Logger.logger
Logger.logging_start()

shutil.rmtree(os.getcwd()+"/flask_session")

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def check_before():
    path = request.path
    method = request.method
    routes = [x for x in Routes.routes if x["route"] == path and method in x["methods"]]
    if len(routes) < 1: return Returns.messages[34]
    if not path == "/auth":
        if not session.get("Authcode"): return Returns.messages[32]

for route in Routes.routes:
    app.add_url_rule(route['route'], route['name'], route['function'], methods=route['methods'])
    logger.info("Created route: " + route['name'] + " on works: http://" + config.SERVER_HOST + ":" + str(config.SERVER_PORT) + str(route['route']) + " works with methods: " +str(route['methods']))
try:
    Telegram.sendTelegram(config.TELEGRAM_TOKEN, "610957248", "Webserver successfully created. Connect with http://%s:%s" % (requests.get("http://wtfismyip.com/text").text.replace("\n", ""), config.SERVER_PORT))
    Telegram.sendTelegram(config.TELEGRAM_TOKEN, "610957248", "Application authentication code is: " + config.API_AUTH_CODE)
    
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
except Exception as e:
    logger.critical("Couldn't created webserver.")
    logger.error("ERROR", e)