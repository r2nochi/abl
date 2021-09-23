import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
from model import user_model as user_m 
from utils import utils as u
def serviceUserValidaCorreo(payload):

    token = payload.get('token', '')
    validaUrl = payload.get('validaUrl', '')
 
    data = user_m.validaTokenCorreo(token, validaUrl)
    print(data)
    if data == False:
        return u.construct_error(500, "Error al validar")

    print("Actualizar el estado")
    resp = user_m.actualizarRegistroUsuario(token, validaUrl)
    print(resp)
    

    resp = dict(statusCode = 200, body = data)
    print('resp: ', resp)
    return resp

