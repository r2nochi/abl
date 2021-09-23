import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg

def insertRegistroUsuario(email, token, datosres, urlVal):
    DB = pg.ConnectionPostgreSql()

    query = '''INSERT INTO public.registrousuario(
	correo, tokenvalidacion, estado, remoteip, serveraddr, useragent, requestmethod, scripturi, serversession, session, urlValidacion)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    estado = "1"
    result = DB.insert(sql = query, values = (email,token, estado,datosres["remote_ip"],datosres["serverAddr"],datosres["userAgent"],datosres["requestMethod"],datosres["scriptUri"], datosres["serverSession"],datosres["session"], urlVal))
    return result    

def buscarEmail(email):
    DB = pg.ConnectionPostgreSql()
    query = '''select * from registrousuario where correo = %s;'''
    
    result = DB.quering(sql = query, values = (email,), fetchtype = 'one')
    if result:
        return True
    else:
        return False

def getUltimoRegistroID():
    DB = pg.ConnectionPostgreSql()
    query = '''SELECT idRegistroUsuario FROM registrousuario ORDER BY idregistrousuario DESC LIMIT 1;'''
    result = DB.quering(sql = query, fetchtype = 'one')

    for k, v in result.items():
        id = v
    return id




    