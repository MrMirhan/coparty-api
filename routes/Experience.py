from flask import request
import sys, time, datetime
sys.path.append('../')
from utils.Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "PUT":
        return add_experience(request.form['user'], request.form['name'], request.form['continent_name'], request.form['company'], request.form['description'], timestamp)