# write all your SQL queries in this file.
from datetime import datetime
from bank import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql

@login_manager.user_loader
def load_user(user_id):
    cur = conn.cursor()
    schema = 'users'
    id = 'id'

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(id))

    cur.execute(user_sql, (int(user_id),))
    if cur.rowcount > 0:
        # return-if svarer til nedenstående:
    		# if schema == 'employees':
    		#   return Employees(cur.fetchone())
    		# else:
    		#   return Customers(cur.fetchone())

        return Users(cur.fetchone()) 
    else:
        return None

class Users(tuple, UserMixin):
    def __init__(self, user_data):
        self.id = user_data[0]
        self.username = user_data[1]
        self.email = user_data[2]
        self.password = user_data[3]
        self.role = "user"

    def get_id(self):
       return (self.id)


def select_Users(username):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Users
    WHERE username = %s OR email = %s
    """
    cur.execute(sql, (username,username))
    user = Users(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return user

def get_unis(): 
    cur = conn.cursor()
    sql = """
    SELECT university_name FROM Universities
    """
    cur.execute(sql)
    unis = [x[0] for x in cur.fetchall()] if cur.rowcount > 0 else None;
    cur.close()
    return unis

