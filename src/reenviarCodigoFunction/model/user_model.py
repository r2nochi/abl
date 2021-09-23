import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg
import secrets

def reenviarCod(id):
    token = (secrets.token_hex(3)).upper()
    urlValida = secrets.token_hex(15)
    print("TOKEN", token)
    print("urlValida", urlValida)
    DB = pg.ConnectionPostgreSql()

    query = ''' UPDATE registrousuario
    SET tokenvalidacion = %s,
    urlvalidacion = %s,
    fechaactualizacion = NOW(),
    tokenuse = false
    WHERE idregistrousuario = %s and tokenuse = false;'''
    result = DB.insert(sql = query, values = (token,urlValida, id))
    d = {}
    d["token"] = token
    d["urlValida"] = urlValida
    return d