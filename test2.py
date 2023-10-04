import mysql.connector
mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'lms1')


   
if mydb.is_connected():
    print('connected to mydql') 
myconn = mydb.cursor()
myconn.execute("SELECT* FROM orders")
output = myconn.fetchall()

for i in output:
    print(i)

'''
myconn = mydb.cursor()
sql_cmd = ("DELETE FROM orders WHERE total_amount = 45")
myconn.execute(sql_cmd)
mydb.commit()
output = myconn.fetchall()

for i in output:
    print(i)
'''
