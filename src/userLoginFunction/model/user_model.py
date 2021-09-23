import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg


def validarEmail(email):
    DB = pg.ConnectionPostgreSql()
    query = '''select idregistrousuario, estado from registrousuario where correo = %s;'''
    
    result = DB.quering(sql = query, values = (email,), fetchtype = 'one')
   
    if result:
        us = {}
        for k, v in result.items():
            
            us[k] = v
        return us
    else:
        return False

def obtenerPassword(idUsuarioRegistro):
    DB = pg.ConnectionPostgreSql()
    query = '''select contrasena from maestrousuarioactivo where fkidusuarioregistro = %s;'''

    result = DB.quering(sql = query, values = (str(idUsuarioRegistro),), fetchtype = 'one')
    if result:
        for k, v in result.items():
            pw = v
            return pw
    else:
        return False




#def getCorreoUsuario(email):
#    DB = pg.ConnectionPostgreSql()
#    query = '''select correo, estado from public.registrousuario where correo = %s and estado = 1'''
#    result = DB.quering(sql = query, values = (email), fetchtype = 'one')
#    return result

#def getContrasenaUsuario(password):
#    DB = pg.ConnectionPostgreSql()
#    query = '''select contrasena from public.maestrousuariohistorico where contrasena = %s'''
#    result = DB.quering(sql = query, values = (password), fetchtype = 'one')
#    return result