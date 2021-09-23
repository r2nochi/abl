import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg
from model import registro_usuario_model as user_res

def insertMaestroUsuario(password, datosres):
    fkid = user_res.getUltimoRegistroID()
    
    DB = pg.ConnectionPostgreSql()
    query = '''INSERT INTO public.maestrousuarioactivo(fkidusuarioregistro, fktipodoc, numdoc, 
    apellidopat, apellidomat,nombre, contrasena,celular, dianacimiento, mesnacimiento, anionacimiento, ciudadnac, 
    pep, codigopostal, fkubigeo, ciudad, direccion, imgdocanv, imgdoinv, selfie, remoteip, serveraddr, useragent, requestmethod, 
    scripturi, serversession, session) VALUES (%s, 1, '', '', '','', %s, '', '', '', '', '', False, '', 1411, '', '', '', '', '', %s, %s, %s, %s, %s, %s, %s);'''
    result = DB.insert(sql = query, values = (fkid, password, datosres["remote_ip"],datosres["serverAddr"],datosres["userAgent"],datosres["requestMethod"],datosres["scriptUri"], datosres["serverSession"],datosres["session"]))
    print(result)
    #Guardar en historico
    u_mas = getUltimoRegistroMaestro()
    
    query = '''INSERT INTO public.maestrousuariohistorico(
	fkidusuarioregistro, fktipodoc, numdoc, apellidopat, apellidomat, nombre, contrasena, celular, dianacimiento, mesnacimiento, anionacimiento, ciudadnac, pep, codigopostal, fkubigeo, ciudad, direccion, imgdocanv, imgdoinv, selfie, fechacreacion, fechaactualizacion, remoteip, serveraddr, useragent, requestmethod, scripturi, serversession, session)
	VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    result_his = DB.insert(sql = query, values = (u_mas['fkidusuarioregistro'], u_mas['fktipodoc'], u_mas['numdoc'], u_mas['apellidopat'], u_mas['apellidomat'], u_mas['nombre'], u_mas['contrasena'],u_mas['celular'], u_mas['dianacimiento'],u_mas['mesnacimiento'], u_mas['anionacimiento'], u_mas['ciudadnac'], u_mas['pep'], u_mas['codigopostal'],u_mas['fkubigeo'], u_mas['ciudad'], u_mas['direccion'], u_mas['imgdocanv'], u_mas['imgdoinv'], u_mas['selfie'], u_mas['fechacreacion'], u_mas['fechaactualizacion'], u_mas['remoteip'], u_mas['serveraddr'], u_mas['useragent'], u_mas['requestmethod'], u_mas['scripturi'], u_mas['serversession'], u_mas['session']))
    print(result_his)
    return result    


def getUltimoRegistroMaestro():
    DB = pg.ConnectionPostgreSql()
    query = '''SELECT * FROM maestrousuarioactivo ORDER BY fkidusuarioregistro DESC LIMIT 1;'''
    result = DB.quering(sql = query, fetchtype = 'one')
    userHis = {}
    for k, v in result.items():
        userHis[k] = v
    return userHis