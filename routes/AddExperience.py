from flask import request
import sys, time, datetime
sys.path.append('../')
from Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        return add_experience(request.form['name'], request.form['continent_name'], request.form['description'], timestamp)