from flask import request
import sys, time, datetime
sys.path.append('../')
from Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        if request.form['profile_type'] == "individual":
            return create_profile_individual(request.form['id'], request.form['mail'], request.form['name'], request.form['surname'], request.form['description'], request.form['image_list'], request.form['interest_list'], request.form['experience_list'], request.form['educational_list'], request.form['profile_package'], timestamp)
    else:
        return {"error": "nop"}