import mysql.connector

class Migration:
    myconn = None

    def mysql_connection(self, host_name, user_name, pswd, dbname):
        self.myconn = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = pswd,
            database = dbname
        )
        return self.myconn
    
    def mysql_select_query(self, table, columns, conditions):
        mycursor = self.myconn.cursor()
        mycursor.execute('SELECT '+columns+' FROM '+table+' WHERE '+conditions)
        results = mycursor.fetchall()
        return results
    
migrate = Migration()
migrate.mysql_connection('localhost', 'navin', 'navin21594', 'myexpenses')
results = migrate.mysql_select_query('expenses', 'title, amount', 'amount > 20')
print(results)
