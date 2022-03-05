from flask import request, session
import sys, time, datetime
sys.path.append('../')
from utils.Functions import *

def main():
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    if request.method == "POST":
        if not session.get("Authcode"):
            if config.API_AUTH_CODE == request.form['authcode']:
                session['Authcode'] = request.form['authcode']
                response = return_messages[30]
                response['json'] = {"code": config.API_AUTH_CODE, "sent": request.form['authcode']}
                return 
            else:
                return return_messages[31]
        else:
            return return_messages[33]
    else:
        return {"error": "nop"}