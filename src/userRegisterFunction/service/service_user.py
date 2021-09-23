import os, binascii
import sys
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)
import secrets
import json
from model import registro_usuario_model as user_res
from model import maestro_usuario_activo_model as user_mae

from utils import utils as u
def serviceUserRegister(payload):
 
    data = {}
    trazaweb =  payload.get("traza_web", '')
    email = payload.get('email', '')
    password = payload.get('password', '')
    datosres = {}
    datosres["remote_ip"] =  payload.get("remote_ip", '')
    datosres["serverAddr"] = payload.get("serverAddr", '')
    datosres["userAgent"] = payload.get("userAgent", '')
    datosres["requestMethod"] = payload.get("requestMethod", '')
    datosres["scriptUri"] = payload.get("scriptUri", '')
    datosres["serverSession"]  = payload.get( "serverSession", '')
    datosres["session"] = payload.get("session", '')

    
    #first_name = payload.get('first_name', '')
    #last_name = payload.get('last_name', '')

    if not u.email_validator(email):
        return u.construct_error(500, "Error en el correo ingresado")
    elif not u.pw_validator(password,8):
        return u.construct_error(500, "Error en la contraseña")
    
    ##Verificar correo no existente
    
    
    if user_res.buscarEmail(email):
        return u.construct_error(500, "Correo ya existe")
   
    ##Generar token
    token = (secrets.token_hex(3)).upper()
    urlValida = secrets.token_hex(15)
    print("TOKEN", token)
    print("urlValida", urlValida)
    ##Enviar correo
    
    
    ## Guardar en registrousuario
    user_registro = user_res.insertRegistroUsuario(email.strip(), token, datosres, urlValida)
    #print('Guardado en registro usuario', user_registro)
    ##GUardar en maestro usuario activo
    ##Guardar en usuario historico
    
    user_maestro = user_mae.insertMaestroUsuario(password.strip(), datosres)
    #print('Guardado en maestro usuario', user_maestro)
    id_last = user_res.getUltimoRegistroID()
    data["id"] = id_last
    data["email"] = email.strip()
    data["token"] = token
    data["urlValida"] = urlValida
    data["message"] = "Registro exitoso"
    
    if user_registro is None or user_maestro is None:
        return u.construct_error(500, "Error al registrar usuario")

    
    resp = dict(statusCode = 200, body = data)
    print('resp: ', resp)
    return resp

