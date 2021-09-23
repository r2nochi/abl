import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg

def validaTokenCorreo(token, validaUrl):
    DB = pg.ConnectionPostgreSql()
    query = '''SELECT idregistrousuario, correo FROM public.registrousuario where tokenvalidacion = %s and urlvalidacion = %s and tokenuse = false and estado = 1'''
    result = DB.quering(sql = query, values = (token, validaUrl), fetchtype = 'one')
    print("RESULT", result)
    if result:
        userHis = {}
        for k, v in result.items():
            userHis[k] = v
        return userHis
    else:
        return False   

def actualizarRegistroUsuario(token, url):
    DB = pg.ConnectionPostgreSql()
    query = ''' UPDATE registrousuario
    SET tokenuse = true,
    estado = 4,
    fechaactualizacion = NOW()
    WHERE tokenvalidacion = %s and urlvalidacion = %s;'''
    result = DB.insert(sql = query, values = (token, url))
    return result