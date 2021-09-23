import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
import traceback as tb
from model import user_model as user_m 
from utils import utils as u
import hashlib
def serviceUserLogin(payload):
    email = payload.get('email', '')
    password = payload.get('password', '')
    salt = "ce74531d"
    password = salt + password
    password = hashlib.md5(password.encode()).hexdigest()
    traza_web = payload.get('traza_web', '')
    us = user_m.validarEmail(email.strip())
    print(us)
    if us == False:
        return u.construct_error(403, "Error en la contraseña")
    
    pw_bd = user_m.obtenerPassword(us["idregistrousuario"])
    
    data = {}
    data["id"] = us["idregistrousuario"]
    data["estado"] = us["estado"]
    data["email"] = email
    #Encriptacion 
    if pw_bd == password:
        resp = dict(statusCode = 200, body = json.dumps({
            'status': 'COMPLETED',
            "data": data
        }))
        print('resp: ', resp)
        return resp
    else:
        return u.construct_error(500, "Error al logearse")

