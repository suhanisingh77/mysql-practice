import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="testuser", password="1234", database="LearnCoding")
db_cursor = mydb.cursor()

db_cursor.execute("select * from Emp")
db_select = db_cursor.fetchall()
print(db_select)