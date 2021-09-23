import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
import traceback as tb
from utils import create_token as ct
from model import tenant_model as tenant_m 

def serviceAuthentication(payload):
    user_tenant = payload.get('user_tenant', '')
    password_tenant = payload.get('password_tenant', '')

    tenant = tenant_m.getTenant(user_tenant.strip(), password_tenant.strip())
    if tenant is None:
        return  dict(statusCode = 401, body = json.dumps({
        'status': 'FAILED',
        'message': 'unauthorized'
        }))
    print('getTenant: ', json.dumps(tenant))

    token = ct.create_access_token(tenant)
    resp = dict(statusCode = 200, body = json.dumps({
        'status': 'COMPLETED',
        'token': token
    }))
    print('response:', resp)
    return resp

