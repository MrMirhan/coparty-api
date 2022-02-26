from flask import request
import sys, time, datetime
sys.path.append('../')
from utils.Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        return add_education(request.form['name'], request.form['continent_name'], int(request.form['type']), request.form['description'], timestamp)