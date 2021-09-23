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
    
        resp = service_u.serviceUserRegister(body)

        if resp["statusCode"] == 200:
            return dict(statusCode = 200, body = json.dumps({
                "status": "COMPLETED",
                "data": resp["body"]
            }))
        else:
            print(resp)
            raise Exception(resp["body"])

    except Exception as e:
        #tb.print_exc(e)
        print("error", e)
        if "FAILED" in str(e):
            er = json.loads(str(e))
            return dict(statusCode = 500, body = json.dumps({
            "status": "FAILED",
            "message": er["message"]
        }))
        
        
        return dict(statusCode = 500, body = json.dumps({
            "status": "FAILED",
            "message": "Un error ha ocurrido"
        }))

if __name__ == "__main__":
    payload = json.dumps({
        "traza_web": "",
        "email": "prueba4@gmail.com",
        "password": "123456789",
        "remote_ip": "",
        "serverAddr": "",
        "userAgent": "",
        "requestMethod":"",
        "scriptUri": "",
        "serverSession": "",
        "session":""
    })
    headers = {
    'x-api-key': '6lLxq76Efr4Fm37m42ply87S3Qettsee9oXQiLZx',
    'Content-Type': 'application/json'
    }
    print(handle({'body': payload}, ''))
