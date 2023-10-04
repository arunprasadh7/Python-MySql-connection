import mysql.connector
mydb = mysql.connector.connect(host='localhost',user = 'root', password = '', database ='student1')

if mydb.is_connected():
    print('connection successful')

'''
myconn = mydb.cursor()
myconn.execute("CREATE DATABASE student1")
'''
'''
myconn = mydb.cursor()
myconn.execute('CREATE TABLE marks (name varchar(255), mark int(10))')
'''
'''
myconn = mydb.cursor()
myconn.execute('ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY')
'''
'''
myconn = mydb.cursor()
myconn.execute('ALTER TABLE marks ADD COLUMN id INT(11) AUTO_INCREMENT PRIMARY KEY')
'''
'''
myconn = mydb.cursor()
myconn.execute("INSERT INTO marks(name, mark) VALUES ('arc',50)" )
mydb.commit()
'''

#inserting multiple values
myconn = mydb.cursor()
myconn.execute("INSERT INTO marks VALUES(DEFAULT, 'Storm',60), (DEFAULT,'Invo',70)")
