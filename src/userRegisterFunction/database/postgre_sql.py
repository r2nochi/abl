import os
import psycopg2
from psycopg2.extras import RealDictCursor

class ConnectionPostgreSql(object):
    rds_host =''
    rds_username =''
    rds_user_pwd = ''
    rds_db_name = ''
    conn_string = ''
    cnn = ''
    def __init__(self):
        self.rds_host = os.environ.get('RDS_HOST') or 'postgresql-develop.c8glzpkwykbs.us-east-1.rds.amazonaws.com'
        self.rds_username = os.environ.get('RDS_USERNAME') or 'develop'
        self.rds_user_pwd = os.environ.get('RDS_USER_PWD') or 'Develop.*'
        self.rds_db_name = os.environ.get('RDS_DB_NAME') or 'desa'

    def connect(self):
        self.cnn = psycopg2.connect(
            host = self.rds_host, 
            user = self.rds_username,
            password = self.rds_user_pwd,
            dbname = self.rds_db_name
        )
        return self.cnn

    def quering(self, sql = '', values = None, fetchtype = 'all'):
        try:
            result = None
            with self.connect() as cnn:
                with cnn.cursor(cursor_factory = RealDictCursor) as cur:
                    print(cur.mogrify(sql, values))
                    if values == None:
                        cur.execute(sql)
                    else:
                        print("dsasd",values)
                        cur.execute(sql, values)
                        

                    if fetchtype == 'one':
                        result = cur.fetchone()
                    elif fetchtype == 'all':
                        result = cur.fetchall()
            return result
        except Exception as e:
            print('error on quering: ', e)
            return None

    def insert(self, sql = '', values = None):
        try:
            rows = None
            with self.connect() as cnn:
                with cnn.cursor(cursor_factory = RealDictCursor) as cur:
                    print(cur.mogrify(sql, values))
                    if values == None:
                        cur.execute(sql)
                    else:
                        cur.execute(sql, values)

                    rows = cur.rowcount
            return rows
        except Exception as e:
            print('error on insert: ', e)
            return None


"""import os
import psycopg2
from psycopg2.extras import RealDictCursor

class ConnectionPostgreSql(object):
    rds_host =''
    rds_username =''
    rds_user_pwd = ''
    rds_db_name = ''
    conn_string = ''
    cnn = ''
    def __init__(self):
        self.rds_host = os.environ.get('RDS_HOST') or 'postgresql-develop.c8glzpkwykbs.us-east-1.rds.amazonaws.com'
        self.rds_username = os.environ.get('RDS_USERNAME') or 'develop'
        self.rds_user_pwd = os.environ.get('RDS_USER_PWD') or 'Develop.*'
        self.rds_db_name = os.environ.get('RDS_DB_NAME') or 'desa'

    def connect(self):
        self.cnn = psycopg2.connect(
            host = self.rds_host, 
            user = self.rds_username,
            password = self.rds_user_pwd,
            dbname = self.rds_db_name
        )
        return self.cnn

    def quering(self, sql = '', values = None, fetchtype = 'all'):
        try:
            result = None
            with self.connect() as cnn:
                with cnn.cursor(cursor_factory = RealDictCursor) as cur:
                    print(cur.mogrify(sql, values))
                    if values == None:
                        cur.execute(sql)
                    else:
                        cur.execute(sql, values)

                    if fetchtype == 'one':
                        result = cur.fetchone()
                    elif fetchtype == 'all':
                        result = cur.fetchall()
            return result
        except Exception as e:
            print('error on quering: ', e)
            return None

    def insert(self, sql = '', values = None):
        try:
            rows = None
            with self.connect() as cnn:
                with cnn.cursor(cursor_factory = RealDictCursor) as cur:
                    print(cur.mogrify(sql, values))
                    if values == None:
                        cur.execute(sql)
                    else:
                        cur.execute(sql, values)

                    rows = cur.rowcount
            return rows
        except Exception as e:
            print('error on insert: ', e)
            return None
"""