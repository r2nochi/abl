import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
import traceback as tb
from service import service_user as service_u 

def handle(event, context):
    try:
        return "Carga exitosa "

    except Exception as e:
        #tb.print_exc(e)
        print("error", e)
        return dict(statusCode = 500, body = json.dumps({
            "status": "FAILED",
            "message": "Un error ha ocurrido"
        }))

if __name__ == "__main__": #para saber si la aplicacion se esta ejecutando principalmente y no esta siendo importada
    payload = json.dumps({
        "email": "dlayza@netdreams.com",   
    })
    headers = {
    'x-api-key': '6lLxq76Efr4Fm37m42ply87S3Qettsee9oXQiLZx',
    'Content-Type': 'application/json'
    }
    handle({'body': payload}, '')