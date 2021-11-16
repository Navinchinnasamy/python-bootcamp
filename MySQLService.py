import os
from dotenv import load_dotenv
import mysql.connector

class MySQLService:
    myconn = None
    
    def __init__(self):
        load_dotenv()
        host = os.getenv('DB_HOST')
        user = os.getenv('DB_USER')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_NAME')
        self.mysql_connection(host, user, password, database)

    def mysql_connection(self, host_name, user_name, pswd, dbname):
        self.myconn = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = pswd,
            database = dbname
        )
        return self.myconn
    
    def mysql_select_query(self, table, columns, limit=10, order_column='', order_dir='ASC', conditions=''):
        mycursor = self.myconn.cursor()
        sql = 'SELECT '+columns+' FROM '+table
        if conditions:
            sql += ' WHERE '+conditions
        elif order_column and order_dir:
            sql += ' ORDER BY '+order_column+' '+order_dir

        sql += ' LIMIT '+str(limit)
        print(sql)
        mycursor.execute(sql)
        results = mycursor.fetchall()
        return results
    
mysql = MySQLService()
print(mysql.myconn)
# migrate.mysql_connection('localhost', 'navin', 'navin21594', 'myexpenses')
# results = mysql.mysql_select_query('expenses', 'title, amount', 3)
#results = mysql.mysql_select_query('expenses', 'title, amount', 3, 'id', 'DESC')
''' results = mysql.mysql_select_query('expenses', 'title, amount', 3, 'id', 'DESC', 'amount > 25')
print(results) '''
