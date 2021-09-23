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
        resp = service_u.serviceUserReenviarCodigo(body)
        print(resp)
        if resp["statusCode"] == 200:
            return dict(statusCode = 200, body = json.dumps({
                "status": "COMPLETED",
                "data": resp["body"]
            }))
        else:
            print(resp)
            raise Exception(resp["body"])

    except Exception as e:
        print(e)
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
        "idUsuario": 24
    })
    headers = {
    'x-api-key': '6lLxq76Efr4Fm37m42ply87S3Qettsee9oXQiLZx',
    'Content-Type': 'application/json'
    }
    print(handle({'body': payload}, ''))
