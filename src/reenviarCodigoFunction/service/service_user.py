import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
from model import user_model as user_m 
from utils import utils as u
def serviceUserReenviarCodigo(payload):

    id = payload.get('idUsuario', '')
 
    d = user_m.reenviarCod(id)
    print(d)
    resp = dict(statusCode = 200, body = d)
    print('resp: ', resp)
    return resp

