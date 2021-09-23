import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
import traceback as tb
from service import service_auth as service_a 

def handle(event, context):
    try:

        body = json.loads(event.get('body'))
        print('body', body)
        result = service_a.serviceAuthentication(body)
        return result

    except Exception as e:
        tb.print_exc(e)
        print("error", e)
        return dict(statusCode = 500, body = json.dumps({
            'status': 'FAILED',
        }))

if __name__ == "__main__":
    payload = json.dumps({
        "user_tenant": "dev",
        "password_tenant": "dev.*",
    })
    headers = {
    'x-api-key': '6lLxq76Efr4Fm37m42ply87S3Qettsee9oXQiLZx',
    'Content-Type': 'application/json'
    }
    handle({'body': payload}, '')
