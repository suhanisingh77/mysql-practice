import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="testuser", password="1234", database="LearnCoding")
db_cursor = mydb.cursor()

db_Updatedata = "update Emp set email=%s where id = %s "
db_value = ("arun1@gmail.com",2)

db_cursor.execute(db_Updatedata, db_value)
mydb.commit()

print(db_cursor.rowcount,"data updated")