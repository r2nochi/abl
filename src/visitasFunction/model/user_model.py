import sys
sys.path.insert(1, '..')
from database import postgre_sql as  pg

def insertUser(email, password, first_name, last_name, status):
    DB = pg.ConnectionPostgreSql()
    query = '''INSERT INTO public.user(email, password, first_name, last_name, status) VALUES(%s,%s,%s,%s, %s)'''
    result = DB.insert(sql = query, values = (email, password, first_name, last_name, status))
    return result    