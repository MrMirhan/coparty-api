from flask import Flask
import config
import time
from routes import index

app = Flask(__name__)

app.add_url_rule("/", "index", index.main)

try:
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, debug=config.SERVER_DEBUG)
    print("Webserver successfully created. Connect with http://%s:%s" % (config.SERVER_HOST, config.SERVER_PORT))
except Exception as e:
    print("Couldn't created webserver.")
    print("ERROR", e)