from flask import request
import sys, time, datetime
sys.path.append('../')
from utils.Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "PUT":
        return put_role(request.form['name'], request.form['continent_name'], request.form['permissions'], request.form['description'], timestamp)
    elif request.method == "GET":
        return get_role(request.form['id'])
    elif request.method == "PATCH":
        return update_role(request.form)
    elif request.method == "POST":
        return add_role(request.form['user'], request.form['id'])