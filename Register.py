from flask import request
import sys, time, datetime
sys.path.append('../')
from Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        return register_validate(request.form['mail'], request.form['conf_mail'], request.form['passwd'], request.form['conf_passwd'], timestamp)
    else:
        return {"error": "nop"}