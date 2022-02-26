from flask import request
import sys, time, datetime
sys.path.append('../')
from utils.Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        return verify_code(request.form['code'], timestamp)
    else:
        return {"error": "nop"}