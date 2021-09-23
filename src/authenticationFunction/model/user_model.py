import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg

def getUser(email, password):
    DB = pg.ConnectionPostgreSql()
    query = '''select * from public.user where email = %s and password = %s and status = true'''
    result = DB.quering(sql = query, values = (email,password), fetchtype = 'one')
    return result    