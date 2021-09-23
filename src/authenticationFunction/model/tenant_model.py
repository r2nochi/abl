
import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg

def getTenant(username,password):
    DB = pg.ConnectionPostgreSql()
    query = '''select * from public.tenant where username = %s and password = %s and status = true'''
    result = DB.quering(sql = query, values = (username,password), fetchtype = 'one')
    return result