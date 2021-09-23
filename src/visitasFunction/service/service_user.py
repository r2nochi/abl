import os
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

import json
from model import user_model as user_m 
from utils import utils as u
def serviceUserRegister(payload):
    email = payload.get('email', '')
    password = payload.get('password', '')
    first_name = payload.get('first_name', '')
    last_name = payload.get('last_name', '')

    if not u.email_validator(email):
        return u.construct_error(500, "Error en el correo ingresado")
    elif not u.pw_validator(password,8):
        return u.construct_error(500, "Error en la contraseña")
        
    user = user_m.insertUser(email.strip(), password.strip(), first_name, last_name, True)
    print('Nuevo usuario', user)
    if user is None:
        return u.construct_error(500, "Error al registrar usuario")

    resp = dict(statusCode = 200, body = json.dumps({
        "status": "COMPLETED",
        "data": {
            "message": "usuario registrado"
        }
    }))
    print('resp: ', resp)
    return resp

