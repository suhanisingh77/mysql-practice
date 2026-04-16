import mysql.connector as MyConn

mydb = MyConn.connect(host="localhost", user="testuser", password="1234", database="LearnCoding")
db_cursor = mydb.cursor()

db_deletedata = "delete from Emp  where id = %s "
db_value = (3,)

db_cursor.execute(db_deletedata, db_value)
mydb.commit()

print(db_cursor.rowcount,"data deleted")