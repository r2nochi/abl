import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
import traceback as tb
from service import service_user as service_u 

def handle(event, context):
    try:
        
        body = json.loads(event.get('body'))
        print('body', body)
        resp = service_u.serviceUserLogin(body)
        return resp

    except Exception as e:
        #tb.print_exc(e)
        print("error", e)
        return dict(statusCode = 500, body = json.dumps({
            'status': 'FAILED',
            "message": 'Un error ha ocurrido'
        }))

if __name__ == "__main__":
    payload = json.dumps({
        "traza_web": "",
        "email": "dtoctoz@gmail.com",
        "password": "12345678"
    })
    headers = {
        'x-api-key': '6lLxq76Efr4Fm37m42ply87S3Qettsee9oXQiLZx',
        'Content-Type': 'application/json'
    }
    print(handle({'body': payload}, ''))